# from faker import Faker
# import random
# from datetime import datetime, timedelta

# # Create a Faker object
# fake = Faker()

# # Function to generate a random date within a given range
# def random_date(start_date, end_date):
#     time_delta = end_date - start_date
#     random_days = random.randint(0, time_delta.days)
#     return start_date + timedelta(days=random_days)

# # Function to generate fake data for the customer table
# def generate_customer_data(num_records):
#     customers = []
#     for _ in range(num_records):
#         customer_name = fake.name()
#         customer_id = fake.unique.random_number(digits=8)
#         customer_address = fake.address()
#         email = fake.email()
#         registration_date = fake.date_between(start_date='-5y', end_date='today')
#         date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=70)
        
#         customer_data = {
#             'customer_name': customer_name,
#             'customer_id': customer_id,
#             'customer_address': customer_address,
#             'email': email,
#             'registration_date': registration_date,
#             'date_of_birth': date_of_birth
#         }
#         customers.append(customer_data)
    
#     return customers

# # Function to generate fake data for the policy_details table
# def generate_policy_details_data(num_records, customer_ids):
#     policies = []
#     for _ in range(num_records):
#         policy_no = fake.unique.random_number(digits=10)
#         policy_description = fake.text(max_nb_chars=50)
#         status = random.choice(['active', 'inactive'])
#         policy_purchase_date = fake.date_between(start_date='-2y', end_date='today')
#         premium = random.uniform(1000, 10000)
#         product = fake.word(ext_word_list=['Health', 'Life', 'Auto', 'Home'])
#         term = random.choice([1, 5, 10, 20])
#         customer_id = random.choice(customer_ids)
        
#         policy_data = {
#             'policy_no': policy_no,
#             'policy_description': policy_description,
#             'status': status,
#             'policy_purchase_date': policy_purchase_date,
#             'premium': premium,
#             'product': product,
#             'term': term,
#             'customer_id': customer_id
#         }
#         policies.append(policy_data)
    
#     return policies

# if __name__ == "__main__":
#     # Set the number of fake records you want to generate
#     num_customers = 20
#     num_policies = 50

#     # Generate fake data for the customer table
#     customers_data = generate_customer_data(num_customers)

#     # Extract customer_ids from the customer data
#     customer_ids = [customer['customer_id'] for customer in customers_data]

#     # Generate fake data for the policy_details table
#     policies_data = generate_policy_details_data(num_policies, customer_ids)

#     # Print the generated data
#     print("Customer Table:")
#     for customer in customers_data:
#         print(customer)

#     print("\nPolicy Details Table:")
#     for policy in policies_data:
#         print(policy)

from faker import Faker
import random
from datetime import datetime, timedelta

# Create a Faker object
fake = Faker()

# Function to generate a random date within a given range
def random_date(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    return start_date + timedelta(days=random_days)

# Function to generate fake data for the customer table
def generate_customer_data(num_records):
    customers = []
    for _ in range(num_records):
        customer_name = fake.name()
        customer_id = fake.unique.random_number(digits=8)
        customer_address = fake.address()
        email = fake.email()
        registration_date = fake.date_between(start_date='-5y', end_date='today')
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=70)
        
        customer_data = {
            'customer_name': customer_name,
            'customer_id': customer_id,
            'customer_address': customer_address,
            'email': email,
            'registration_date': registration_date,
            'date_of_birth': date_of_birth
        }
        customers.append(customer_data)
    
    return customers

# Function to generate fake data for cover components
def generate_cover_components(num_components):
    components = []
    for _ in range(num_components):
        component_name = fake.word(ext_word_list=['Fire', 'Theft', 'Accident', 'Life'])
        component_premium = random.uniform(100, 500)
        component_data = {
            'component_name': component_name,
            'component_premium': component_premium
        }
        components.append(component_data)
    return components

# Function to generate fake data for the policy_details table
def generate_policy_details_data(num_records, customer_ids):
    policies = []
    for _ in range(num_records):
        policy_no = fake.unique.random_number(digits=10)
        policy_description = fake.text(max_nb_chars=50)
        status = random.choice(['active', 'inactive'])
        policy_purchase_date = fake.date_between(start_date='-2y', end_date='today')
        premium = random.uniform(1000, 10000)
        product = fake.word(ext_word_list=['Health', 'Life', 'Auto', 'Home'])
        term = random.choice([1, 5, 10, 20])
        customer_id = random.choice(customer_ids)

        # Generate data for cover
        num_covers = random.randint(1, 3)
        covers = []
        for _ in range(num_covers):
            cover_id = fake.unique.random_number(digits=5)
            cover_status = random.choice(['active', 'inactive'])
            cover_product = fake.word(ext_word_list=['Fire', 'Theft', 'Accident', 'Life'])
            premium_amount = random.uniform(500, 2000)
            cover_start_date = fake.date_between(start_date='-1y', end_date='today')
            cover_end_date = cover_start_date + timedelta(days=random.randint(60, 365))
            num_components = random.randint(1, 4)
            cover_components = generate_cover_components(num_components)

            cover_data = {
                'cover_id': cover_id,
                'cover_status': cover_status,
                'cover_product': cover_product,
                'premium_amount': premium_amount,
                'cover_start_date': cover_start_date,
                'cover_end_date': cover_end_date,
                'cover_components': cover_components
            }
            covers.append(cover_data)

        policy_data = {
            'policy_no': policy_no,
            'policy_description': policy_description,
            'status': status,
            'policy_purchase_date': policy_purchase_date,
            'premium': premium,
            'product': product,
            'term': term,
            'customer_id': customer_id,
            'covers': covers
        }
        policies.append(policy_data)
    
    return policies

if __name__ == "__main__":
    # Set the number of fake records you want to generate
    num_customers = 20
    num_policies = 5

    # Generate fake data for the customer table
    customers_data = generate_customer_data(num_customers)

    # Extract customer_ids from the customer data
    customer_ids = [customer['customer_id'] for customer in customers_data]

    # Generate fake data for the policy_details table
    policies_data = generate_policy_details_data(num_policies, customer_ids)

    # Print the generated data
    print("Customer Table:")
    for customer in customers_data:
        print(customer)

    print("\nPolicy Details Table:")
    for policy in policies_data:
        print(policy)

