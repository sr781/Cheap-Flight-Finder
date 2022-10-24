# Cheap-Flight-Finder
If a flight is found where the destination is on Google sheets and the price is below the threshold, a text message is sent informing the recipient. Flight data is requested and obtained via an API from KIWI flights. This project incorporates: application programming interface for getting data from the Google sheets file, flight data information from Tequila and Twilio to send the text message.


![image](https://user-images.githubusercontent.com/96390217/187093711-5a5f3c9f-0f60-4500-928d-9490774fe85c.png)

Figure 1: The Google sheets file with the destination and minimum price threshold


![image](https://user-images.githubusercontent.com/96390217/187093752-b22fa98b-02aa-45c4-89b2-3cc88dcbdb98.png)

Figure 2: The console when the program is run

From figure 2, it can be seen that the price for a Paris trip is £60 which is less than the £65 threshold so a text message is sent to the user. The rest are all above the threshold so no text messages are sent.

![image](https://user-images.githubusercontent.com/96390217/187093857-a12e58c8-ba10-4827-b4fd-46e7a7ae46e3.png)

Figure 3: The text message content shown to the recipient if a flight deal is found


The links below are the API programs used for this project:

(1)  https://partners.kiwi.com/our-solutions/tequila/

(2)  https://sheety.co/

(3)  https://www.twilio.com/
