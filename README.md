# MusicGuru
Simple client server pair for music storage

Made to run on an AWS instance
stores a list of songs grouped by year

MusicGuruServer <portNumber> sets up the server to listen on the specified port number

MusicGuruClient <IP> <Port> <Year> Initilises the client to send a request to the server given the requested year

The	server will loop forever around an accept method call, which will pause the server
until	a	connection	request	is	made	from	a	client.	Once	the	request	
is accepted, it sends the	year range of the dataset	to the client via	the	socket.				
The	client chooses a year	from the range and sends that	to the server.		
If it	turns out	this was within	the	range	the	server sent, it requests that year.
Otherwise	the	client generates a random	year from	the	range.	
For instance you can give	the	year as	0, and	you’ll just get	a	random top ten	
song from	a	random year.
