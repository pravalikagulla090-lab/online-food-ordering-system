from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from menu.models import Restaurant, Category, MenuItem

User = get_user_model()

class Command(BaseCommand):
    help = 'Populates the database with restaurants, categories, and South Indian menu items.'

    def handle(self, *args, **kwargs):
        self.stdout.write('🧹 Purging old restaurant catalog records...')
        MenuItem.objects.all().delete()
        Category.objects.all().delete()
        Restaurant.objects.all().delete()

        def create_owner(username, email):
            user = User.objects.filter(username=username).first()
            if not user:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password='securepassword123'
                )
            return user

        self.stdout.write('👤 Creating restaurant owners...')
        owners = [
            create_owner('dakshin_owner', 'dakshin@foodproject.com'),
            create_owner('coconut_owner', 'coconut@foodproject.com'),
            create_owner('chennai_owner', 'chennai@foodproject.com'),
            create_owner('madras_owner', 'madras@foodproject.com'),
            create_owner('udupi_owner', 'udupi@foodproject.com'),
            create_owner('burger_manager', 'burger@foodproject.com'),
            create_owner('pizza_manager', 'pizza@foodproject.com'),
            create_owner('wok_manager', 'wok@foodproject.com'),
            create_owner('chaat_manager', 'chaat@foodproject.com'),
            create_owner('green_manager', 'green@foodproject.com'),
            create_owner('sweet_manager', 'sweet@foodproject.com'),
            create_owner('wrap_manager', 'wrap@foodproject.com'),
            create_owner('brew_manager', 'brew@foodproject.com'),
            create_owner('north_manager', 'north@foodproject.com'),
            create_owner('tandoor_manager', 'tandoor@foodproject.com'),
        ]

        self.stdout.write('🌱 Creating categories...')
        category_titles = [
            'South Indian',
            'North Indian',
            'Burgers & Sliders',
            'Pizzas & Pasta',
            'Chinese',
            'Street Food',
            'Beverages',
            'Desserts',
            'Wraps & Rolls',
            'Salads & Bowls',
        ]
        categories = {title: Category.objects.create(title=title) for title in category_titles}

        self.stdout.write('🏪 Creating restaurants...')
        restaurants_data = [
            {
                'name': 'Dakshin Delights',
                'address': '21 Spice Lane, South Town',
                'contact': '+91-98765-43210',
                'owner': owners[0],
                'description': 'Authentic South Indian plates served with coconut chutney and sambar.',
            },
            {
                'name': 'Coconut Grove South Kitchen',
                'address': '38 Filter Coffee Street, Old City',
                'contact': '+91-91234-56789',
                'owner': owners[1],
                'description': 'Coastal South Indian menu with fresh curry leaves and coconut flavors.',
            },
            {
                'name': 'Chennai Spice House',
                'address': '105 Marina Road, Harbor District',
                'contact': '+91-99887-66554',
                'owner': owners[2],
                'description': 'Madras-style masalas, tiffin specials, and crunchy vadas.',
            },
            {
                'name': 'Madras Masala Room',
                'address': '64 Dravidian Avenue, Food Quarter',
                'contact': '+91-94455-22331',
                'owner': owners[3],
                'description': 'Spicy Chettinad curries and slow-cooked South Indian specialties.',
            },
            {
                'name': 'Udupi Palace',
                'address': '12 Karnataka Street, Temple Town',
                'contact': '+91-91122-33445',
                'owner': owners[4],
                'description': 'Vegetarian South Indian classics with an Udupi twist.',
            },
            {
                'name': 'The Burger Billionaire',
                'address': '102 Gourmet Boulevard, Foodie District',
                'contact': '+1-555-0192',
                'owner': owners[5],
                'description': 'Premium patties, artisan buns, and loaded fries.',
            },
            {
                'name': 'Pizzeria Bella Italia',
                'address': '456 Roma Way, Little Italy',
                'contact': '+1-555-0143',
                'owner': owners[6],
                'description': 'Wood-fired pizzas with authentic Italian toppings.',
            },
            {
                'name': 'Wok This Way',
                'address': '77 Dragon Court, Chinatown',
                'contact': '+91-99872-44221',
                'owner': owners[7],
                'description': 'Stir-fried noodles, dumplings, and wok-crisp vegetables.',
            },
            {
                'name': 'Chaat Bazaar',
                'address': '9 Spice Market Road, Bazaar Lane',
                'contact': '+91-90001-22334',
                'owner': owners[8],
                'description': 'Street food flavors from pani puri to chole bhature.',
            },
            {
                'name': 'Greens & Grains',
                'address': '56 Wellness Way, Green Park',
                'contact': '+91-98811-66778',
                'owner': owners[9],
                'description': 'Healthy bowls, salads, and fresh juices for mindful eaters.',
            },
            {
                'name': 'Sweet Spot Desserts',
                'address': '18 Sugar Street, Dessert District',
                'contact': '+91-97777-88990',
                'owner': owners[10],
                'description': 'Decadent desserts, shakes, and plated sweets.',
            },
            {
                'name': 'Mediterranean Wrap Co.',
                'address': '32 Wrap Avenue, Flavor Plaza',
                'contact': '+91-96666-12345',
                'owner': owners[11],
                'description': 'Fresh wraps, rolls, and grilled Mediterranean plates.',
            },
            {
                'name': 'Brewhouse Beverages',
                'address': '222 Chill Street, Beverage Block',
                'contact': '+91-98822-33445',
                'owner': owners[12],
                'description': 'Cold brews, smoothies, and signature mocktails.',
            },
            {
                'name': 'North Spice Kitchen',
                'address': '88 Heritage Road, Curry Lane',
                'contact': '+91-99988-77665',
                'owner': owners[13],
                'description': 'Rich North Indian classics, naan breads, and tandoor specialties.',
            },
            {
                'name': 'Tandoor Trail',
                'address': '12 Clay Oven Street, Taste Town',
                'contact': '+91-92233-44556',
                'owner': owners[14],
                'description': 'Smoky tandoori platters and biryani bowls.',
            },
        ]

        restaurants = {}
        for data in restaurants_data:
            restaurants[data['name']] = Restaurant.objects.create(**data)

        self.stdout.write('🍽️ Populating South Indian menu items...')
        south_items = [
            ('Dakshin Delights', 'South Indian', 'Plain Dosa', 'Crispy fermented rice and lentil crepe served with sambar and chutneys.', 129.00, True),
            ('Dakshin Delights', 'South Indian', 'Masala Dosa', 'Potato masala stuffed dosa with coconut chutney and sambar.', 159.00, True),
            ('Dakshin Delights', 'South Indian', 'Mysore Masala Dosa', 'Spicy chutney smeared dosa with potato filling and coconut chutney.', 169.00, True),
            ('Dakshin Delights', 'South Indian', 'Set Dosa', 'Soft double dosas with coconut chutney and vegetable sambar.', 149.00, True),
            ('Dakshin Delights', 'South Indian', 'Onion Uttapam', 'Thick rice pancake topped with onions, tomatoes and chilies.', 139.00, True),
            ('Dakshin Delights', 'South Indian', 'Rava Masala Dosa', 'Semolina dosa filled with spicy potato masala and chutney.', 169.00, True),
            ('Dakshin Delights', 'South Indian', 'Neer Dosa', 'Soft rice crepes served with coconut chutney and vegetable stew.', 139.00, True),
            ('Dakshin Delights', 'South Indian', 'Medu Vada', 'Lentil doughnut served with sambar and chutney.', 119.00, True),
            ('Coconut Grove South Kitchen', 'South Indian', 'Idli Sambar', 'Steamed rice cakes with piping hot sambar and coconut chutney.', 129.00, True),
            ('Coconut Grove South Kitchen', 'South Indian', 'Mini Idli', 'Mini idlis tossed with ghee and spice powder.', 129.00, True),
            ('Coconut Grove South Kitchen', 'South Indian', 'Paniyaram Platter', 'Crispy and soft appams served with chutney and sambar.', 149.00, True),
            ('Coconut Grove South Kitchen', 'South Indian', 'Masala Pesarattu', 'Green gram crepe filled with spicy onion masala.', 159.00, True),
            ('Coconut Grove South Kitchen', 'South Indian', 'Akki Roti', 'Rice flour roti flavored with onions, chilies, and coconut.', 149.00, True),
            ('Coconut Grove South Kitchen', 'South Indian', 'Kanchipuram Idli', 'Spiced steamed idlis infused with pepper and cumin.', 139.00, True),
            ('Coconut Grove South Kitchen', 'South Indian', 'Tomato Rice', 'Tangy tomato rice with curry leaves and peanuts.', 139.00, True),
            ('Coconut Grove South Kitchen', 'South Indian', 'Coconut Rice', 'Fragrant rice cooked with fresh coconut and spices.', 149.00, True),
            ('Chennai Spice House', 'South Indian', 'Sambar Vada', 'Crispy vada soaked in tangy sambar and garnished with onions.', 149.00, True),
            ('Chennai Spice House', 'South Indian', 'Rasam Rice', 'Peppery rasam served over steamed rice with papad.', 139.00, True),
            ('Chennai Spice House', 'South Indian', 'Curd Rice', 'Cooling yoghurt rice tempered with mustard seeds and curry leaves.', 129.00, True),
            ('Chennai Spice House', 'South Indian', 'Lemon Rice', 'Tangy lemon rice tossed with curry leaves and nuts.', 139.00, True),
            ('Chennai Spice House', 'South Indian', 'Puliyodarai', 'Tamarind rice with peanuts and aromatic spices.', 149.00, True),
            ('Chennai Spice House', 'South Indian', 'Ven Pongal', 'Creamy rice and lentil dish tempered with ghee and spices.', 139.00, True),
            ('Chennai Spice House', 'South Indian', 'Rava Upma', 'Semolina upma with vegetables and cashews.', 129.00, True),
            ('Chennai Spice House', 'South Indian', 'Coconut Chutney Trio', 'Three chutneys served with your choice of dosa or idli.', 99.00, True),
            ('Madras Masala Room', 'South Indian', 'Chapati Masala', 'Freshly made chapatis tossed with flavorful masala.', 169.00, True),
            ('Madras Masala Room', 'South Indian', 'Khodu Kasu', 'Spicy Kerala-style banana chips and coconut relish.', 129.00, True),
            ('Madras Masala Room', 'South Indian', 'Fish Curry', 'Coastal fish curry cooked in tangy tamarind spices.', 299.00, False),
            ('Madras Masala Room', 'South Indian', 'Prawn Varuval', 'Dry prawns tossed in spicy South Indian masala.', 329.00, False),
            ('Madras Masala Room', 'South Indian', 'Chicken Chettinad', 'Rich chicken curry with roasted spices and coconut.', 289.00, False),
            ('Madras Masala Room', 'South Indian', 'Egg Roast', 'Boiled eggs simmered in aromatic masala gravy.', 199.00, False),
            ('Madras Masala Room', 'South Indian', 'Appam & Stew', 'Soft appams served with coconut vegetable stew.', 239.00, True),
            ('Udupi Palace', 'South Indian', 'Masala Vada', 'Spiced lentil doughnuts with curry leaf seasoning.', 119.00, True),
            ('Udupi Palace', 'South Indian', 'Tomato Saaru', 'South Indian tomato soup served with rice.', 129.00, True),
            ('Udupi Palace', 'South Indian', 'Green Gram Sundal', 'Seasoned split green gram salad with coconut.', 109.00, True),
            ('Udupi Palace', 'South Indian', 'Mysore Bonda', 'Soft lentil fritters with coconut chutney.', 129.00, True),
            ('Udupi Palace', 'South Indian', 'Idli Fry', 'Shallow-fried idlis tossed in spices and curry leaves.', 139.00, True),
            ('Udupi Palace', 'South Indian', 'Vegetable Kurma', 'Creamy coconut vegetable kurma served with dosa.', 159.00, True),
            ('Udupi Palace', 'South Indian', 'Pongal Rice Bowl', 'Sweet and savory pongal with ghee and pepper.', 149.00, True),
        ]

        for restaurant_name, category_title, name, description, price, is_veg in south_items:
            MenuItem.objects.create(
                restaurant=restaurants[restaurant_name],
                category=categories[category_title],
                name=name,
                description=description,
                price=price,
                is_veg=is_veg,
            )

        self.stdout.write('🍔 Populating additional categories and restaurants...')
        additional_items = [
            ('The Burger Billionaire', 'Burgers & Sliders', 'Smoked BBQ Bacon Burger', 'Charcoal-grilled beef patty with smoky BBQ sauce.', 249.00, False),
            ('The Burger Billionaire', 'Burgers & Sliders', 'Plant-Based Super Burger', 'Grilled plant patty with avocado and almond aioli.', 229.00, True),
            ('Pizzeria Bella Italia', 'Pizzas & Pasta', 'Four Cheese Quattro Formaggi', 'Mozzarella, parmesan, gorgonzola, and ricotta pizza.', 449.00, True),
            ('Pizzeria Bella Italia', 'Pizzas & Pasta', 'Spicy Arrabiata Pasta', 'Penne tossed in a fiery tomato garlic sauce.', 289.00, True),
            ('Wok This Way', 'Chinese', 'Schezuan Noodles', 'Stir-fried noodles in hot Schezuan sauce.', 219.00, False),
            ('Wok This Way', 'Chinese', 'Vegetable Dumplings', 'Steamed dumplings with ginger-soy dipping sauce.', 199.00, True),
            ('Chaat Bazaar', 'Street Food', 'Paneer Tikka Chaat', 'Tandoori paneer tossed with chutneys and sev.', 189.00, True),
            ('Chaat Bazaar', 'Street Food', 'Aloo Tikki Chole', 'Potato patties topped with chickpea curry.', 159.00, True),
            ('Greens & Grains', 'Salads & Bowls', 'Quinoa Power Bowl', 'Quinoa, roasted vegetables, avocado and tahini.', 249.00, True),
            ('Greens & Grains', 'Salads & Bowls', 'Halloumi Grain Salad', 'Grilled halloumi with farro and mixed greens.', 269.00, False),
            ('Sweet Spot Desserts', 'Desserts', 'Chocolate Lava Cake', 'Warm chocolate cake with molten center.', 179.00, True),
            ('Sweet Spot Desserts', 'Desserts', 'Mango Kulfi', 'Creamy mango ice cream with pistachio crunch.', 149.00, True),
            ('Mediterranean Wrap Co.', 'Wraps & Rolls', 'Falafel Shawarma Wrap', 'Crispy falafel with tahini and pickled veggies.', 209.00, True),
            ('Mediterranean Wrap Co.', 'Wraps & Rolls', 'Chicken Gyro Roll', 'Marinated chicken, tzatziki, and salad in flatbread.', 229.00, False),
            ('Brewhouse Beverages', 'Beverages', 'Cold Brew Latte', 'Smooth cold brew with almond milk.', 159.00, True),
            ('Brewhouse Beverages', 'Beverages', 'Mango Lassi', 'Refreshing sweet mango yogurt drink.', 139.00, True),
            ('North Spice Kitchen', 'North Indian', 'Butter Chicken', 'Creamy tomato-based chicken curry.', 319.00, False),
            ('North Spice Kitchen', 'North Indian', 'Paneer Lababdar', 'Cottage cheese in velvety tomato gravy.', 289.00, True),
            ('Tandoor Trail', 'North Indian', 'Lamb Seekh Kebab', 'Spiced minced lamb skewers from the tandoor.', 339.00, False),
            ('Tandoor Trail', 'North Indian', 'Tandoori Mushroom', 'Charred mushrooms with tandoori spices.', 229.00, True),
        ]

        for restaurant_name, category_title, name, description, price, is_veg in additional_items:
            MenuItem.objects.create(
                restaurant=restaurants[restaurant_name],
                category=categories[category_title],
                name=name,
                description=description,
                price=price,
                is_veg=is_veg,
            )

        self.stdout.write(self.style.SUCCESS('🎉 Database populated with 15 restaurants, 10 categories, and 35 South Indian items.'))
