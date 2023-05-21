# Leacture 5 - Work hard to fulfill your desires
 
In the realm of achieving our goals, it is imperative that we take the initiative to create and build something on our own. Without this willingness to venture into uncharted territory, we risk falling short of our desired aspirations. By embarking on the journey of constructing a project from scratch, we unlock a gateway to the world of Full Stack development and set ourselves on a path towards realizing our dreams. It is through these endeavors that we discover our true potential and pave the way for future accomplishments. Therefore, it is essential to embrace the challenge and make that first step, for it is in our own hands that the power to shape our future lies.


## User Requirements - Online shop for selling cars (Project Name: luxury_cars)

When undertaking a project for a client, it is crucial to recognize that they may not possess a comprehensive understanding of the programming world. As the developer, it becomes your responsibility to bridge this gap effectively. The client will convey their requirements and expectations, and it is up to you to translate and adapt them into the language of programming. This process necessitates clear communication, active listening, and a deep comprehension of both the client's needs and the technical aspects involved. By successfully transferring their demands into the programming realm, you can create a harmonious collaboration that ensures the final product aligns with their vision while leveraging your expertise to deliver a functional and user-friendly solution.

- Cars should have owners. An owner can own one or more cars.
- An owner's profile includes their full name, contact number, city, a wallet starting with zero money, and a unique profile identifier (slug).
- A car should have unique characteristics like model, color, price, production year, image, and a unique slug for the car details page.
- Customers are users who can buy cars from owners. A customer profile includes their full name, contact number, city, a wallet starting with $1000, and a count of cars bought initially set to zero.
- The header should display the number of cars a customer has bought.
- When a car is bought, remove it from the owner's list, add its price to the owner's wallet, deduct its price from the customer's wallet, and increase the count of cars the customer owns by one. Ensure the customer can afford the car.
- An owner's profile page should show their full name, contact number, city, email, and a list of their cars.
- An owner should be able to delete their cars from their profile page. Only car owners can delete cars.
- Create a homepage that lists all cars. Users should be able to search cars by production year. Each car listing should link to the owner's profile page.
- Include a 'add new car' link in the header, accessible only to car owners.
- Create a car details page for each car showing all its characteristics. The page's URL should use the car's unique slug.
- Create a registration page for both customers and owners. During registration, users should select their role and specify their starting wallet amount.
- Include a login page requiring a username and password.
- Create a profile editing page for owners, allowing them to change their names. Only the profile owner can make changes.
