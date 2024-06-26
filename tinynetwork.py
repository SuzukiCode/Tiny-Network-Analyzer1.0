from scapy.all import *
import os
import pyfiglet

def print_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

def capture_and_save_packets(save_dir, save_file):
    try:
        # Print listening message
        print("\nListening to network traffic for 60 seconds...")

        # Sniff packets on all interfaces for 60 seconds
        packets = sniff(iface=None, timeout=60, prn=lambda x: x.summary(), store=1)

        # Prompt user for directory to save pcap file
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Construct full path including directory and filename
        save_path = os.path.join(save_dir, save_file)

        # Write packets to pcap file
        wrpcap(save_path, packets)

        print(f"\nPackets saved to {save_path}")

    except KeyboardInterrupt:
        print("\nCapture interrupted by user.")

    except Exception as e:
        print(f"Error capturing or saving packets: {e}")

def main():
    try:
        # Print ASCII art
        print_ascii_art("Tiny Network Analyzer")

        # Prompt user for directory and filename to save the captured packets
        save_dir = input("Enter the directory path to save the captured packets (e.g., C:\\CapturedPackets\\): ")
        save_file = input("Enter a filename for the captured packets (e.g., captured_traffic.pcap): ")

        # Capture and save packets
        capture_and_save_packets(save_dir, save_file)

    except KeyboardInterrupt:
        print("\nCapture interrupted by user.")

    # Wait for user input before exiting
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()






