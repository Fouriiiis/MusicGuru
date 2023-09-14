import socket
import sys
import random

def validate_year_range(year_range):
    try:
        min_year, max_year = map(int, year_range.split('-'))
        return min_year, max_year
    except ValueError:
        return None, None

def get_random_year(min_year, max_year):
    return random.randint(min_year, max_year)

def main():
    if len(sys.argv) < 3:
        print("Usage: python MusicGuruClient.py <server_ip> <server_port> [year]")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    # Create a socket connection to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # Receive the year range from the server
    year_range = client_socket.recv(1024).decode()
    min_year, max_year = validate_year_range(year_range)

    if min_year is None or max_year is None:
        print("Invalid year range received from the server.")
        client_socket.close()
        sys.exit(1)

    # Determine the year to request
    if len(sys.argv) == 4:
        year = int(sys.argv[3])
        if year < min_year or year > max_year:
            year = get_random_year(min_year, max_year)
            #specified year out of range (min_year, max_year), using random year instead: {random_year}
            print(f"Specified year out of range ({min_year}, {max_year}), using random year instead: {year}")
            
    else:
        year = get_random_year(min_year, max_year)

    # Send the selected year to the server
    client_socket.send(str(year).encode())

    # Receive and display the song from the server
    #{song_position} {song} {year} {private_address}
    song_info = client_socket.recv(1024).decode()
    #output the song info in a nice format
    #in {year} the number {song_position} song was {song}
    #use the year sent to the server
    #song is all the info after the song position and before the private address
    #private address is the last thing sent
    song_info = song_info.split()
    song_position = song_info[0]
    song = " ".join(song_info[1:-1])
    private_address = song_info[-1]
    print(f"In {year} the number {song_position} song was {song}")
    print(f"Server private address: {private_address}")



    # Close the socket connection
    client_socket.close()

if __name__ == "__main__":
    main()
