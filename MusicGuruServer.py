import socket
import sys
import random

# Define a dictionary to store songs by year
songs_by_year = {
    2000: ["Song A", "Song B", "Song C"],
    2001: ["Song D", "Song E", "Song F"],
    2002: ["Song G", "Song H", "Song I"],
    2003: ["Song J", "Song K", "Song L"],
    2004: ["Song M", "Song N", "Song O"],
    2005: ["Song P", "Song Q", "Song R"],
    2006: ["Song S", "Song T", "Song U"],
    2007: ["Song V", "Song W", "Song X"],
    2008: ["Song Y", "Song Z", "Song AA"],
    2009: ["Song BB", "Song CC", "Song DD"],
    2010: ["Song EE", "Song FF", "Song GG"],
}

# Function to validate a port number
def validate_port(port):
    try:
        port = int(port)
        if 0 < port <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False

# Function to send the year range to the client
def send_year_range(client_socket):
    years = list(songs_by_year.keys())
    year_range = f"{min(years)}-{max(years)}"
    client_socket.send(year_range.encode())

# Function to send a random song from a specific year to the client
def send_random_song(client_socket, year):
    if year in songs_by_year:
        # Send a random song from the year along with its position in the list
        song = random.choice(songs_by_year[year])
        song_position = songs_by_year[year].index(song) + 1
        # get the private address of the server
        private_address = socket.gethostbyname(socket.gethostname())
        client_socket.send(f"{song_position} {song} {private_address}".encode())
    else:
        client_socket.send("Year not found".encode())

def main():
    if len(sys.argv) != 2:
        print("Usage: python MusicGuruServer.py <port>")
        sys.exit(1)

    port = sys.argv[1]

    if not validate_port(port):
        print("Invalid port number. Please use a valid port number (1-65535).")
        sys.exit(1)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', int(port)))
    server_socket.listen(5)
    print(f"Listening on port {port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Send the year range to the client
        send_year_range(client_socket)

        # Receive the selected year from the client
        year_data = client_socket.recv(1024).decode()
        year = int(year_data)

        # Send a random song from the selected year to the client
        send_random_song(client_socket, year)

        client_socket.close()

if __name__ == "__main__":
    main()
