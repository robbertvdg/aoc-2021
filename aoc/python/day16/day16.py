from typing import List, Any
import numpy as np


def decode_hex(hex: str) -> str:
    decode_dict = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    result_str = ''
    for char in hex:
        result_str += decode_dict[char]
    return result_str


class Packet:
    version: int
    packet_id: int
    bit_length: int
    is_literal: bool
    sub_packets: List[Any]

    def __init__(self, binary_string: str):
        self.sub_packets = []
        self.version = int(binary_string[0:3], 2)
        self.packet_id = int(binary_string[3:6], 2)
        if self.packet_id == 4:
            self.is_literal = True
            done = False
            bits = ""
            i = 6
            while not done:
                if binary_string[i] == "0":
                    done = True
                bits += binary_string[i + 1:i + 5]
                i = i + 5
            self.sub_packets.append(int(bits, 2))
            self.bit_length = i
        else:
            self.is_literal = False
            length_id = binary_string[6]
            self.bit_length = 7
            if length_id == '0':
                length = int(binary_string[7:22], 2)
                self.bit_length += length + 15
                index = 22
                done = False
                while not done:
                    packet = Packet(binary_string[index:])
                    self.sub_packets.append(packet)
                    if index + packet.bit_length == 22 + length:
                        done = True
                    index = index + packet.bit_length
            else:
                nr_packets = int(binary_string[7:18], 2)
                self.bit_length += 11
                index = 18
                for _ in range(nr_packets):
                    packet = Packet(binary_string[index:])
                    index += packet.bit_length
                    self.bit_length += packet.bit_length
                    self.sub_packets.append(packet)

    def get_version_sum(self):
        summed = self.version
        if not self.is_literal:
            for packet in self.sub_packets:
                summed += packet.get_version_sum()
        return summed

    def get_packet_value(self):
        if self.packet_id == 0:
            return sum([x.get_packet_value() for x in self.sub_packets])
        elif self.packet_id == 1:
            return np.prod([x.get_packet_value() for x in self.sub_packets])
        elif self.packet_id == 2:
            return min([x.get_packet_value() for x in self.sub_packets])
        elif self.packet_id == 3:
            return max([x.get_packet_value() for x in self.sub_packets])
        elif self.packet_id == 4:
            return self.sub_packets[0]
        elif self.packet_id == 5:
            return self.sub_packets[0].get_packet_value() > self.sub_packets[1].get_packet_value()
        elif self.packet_id == 6:
            return self.sub_packets[0].get_packet_value() < self.sub_packets[1].get_packet_value()
        else:
            return self.sub_packets[0].get_packet_value() == self.sub_packets[1].get_packet_value()


def read_input(path: str) -> (str, dict):
    with open(path, "r") as f:
        return f.read().strip()


if __name__ == "__main__":
    input_hex = read_input("./input.txt")
    input_string = decode_hex(input_hex)
    packet = Packet(input_string)
    answer1 = packet.get_version_sum()
    answer2 = packet.get_packet_value()
    print(f"The answer to day 16 puzzle 1: {answer1}")
    print(f"The answer to day 16 puzzle 2: {answer2}")
