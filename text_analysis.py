from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import ipdb

class TextAnalysis():

    def __init__(self):
        self.data = [
            ("Walmart Fruits Vegetables and Groceries", "Groceries"),
            ("Kroger Fred Meyer Ralphs groceries", "Groceries"),
            ("Albertsons Farmers Market ", "Groceries"),
            ("Costco Fruits and Vegetables", "Groceries"),
            ("Target Groceries Markets ", "Groceries"),
            ("Amazon Groceries", "Groceries"),
            ("Safeway Fruits and Vegetables and Groceries", "Groceries"),
            ("Trader Joe's Fruits and Vegetables", "Groceries"),
            ("Whole Foods Market Fruits and Vegetables", "Groceries"),

            ("Movies and Cinema ", "Entertainment"),
            ("Listening to Songs", "Entertainment"),
            ("Amusement and Trampoline Parks", "Entertainment"),
            ("Clubs and Parties", "Entertainment"),
            ("Online Streaming Services Subscriptions", "Entertainment"),
            ("New Movie At The Movie Theaters", "Entertainment"),
            ("Jazz Concert And Symphony shows and concerts", "Entertainment"),
            ("Board game purchase", "Entertainment"),
            ("Escape room experience", "Entertainment"),

            ("Mexican Taco Burrito Enchiladas Guacamole Quesadillas ", "Eating Out"),
            ("Fast Food Fries Chicken Beef Pork Burgers wings fire Hotdogs sauce juicy", "Eating Out"),
            ("Sandwiches Express Roasted Vegetables Salads Cheese", "Eating Out"),
            ("Italian Pasta Pizza Pepperoni Margherita Spaghetti soups stews Risotto", "Eating Out"),
            ("Blizzards Icecream Tiramasu Chocolate brownie cookie ", "Eating Out"),
            ("Thai curry PadThai Panang PadSeeEw  Rice", "Eating Out"),
            ("Chinese Takeout Noodles dimsum Fish Animals", "Eating Out"),
            ("Mediterranean Indian Naan Fried Roasted Toasted Grilled", "Eating Out"),
            ("Tea Boba Cocktail Mocktail Alcohol Soda Juice", "Eating Out"),
            ("Korean Donuts Sweets Creme Middle Eastern", "Eating Out"),

            ("Uber Lyft Taxis Traveling Shifting Moving", "Transportation"),
            ("Train Movement Plane Air Flying", "Transportation"),
            ("Bus Rides Carpools Venmo Payments", "Transportation"),
            ("Subways Metroes and Ferries Biking", "Transportation"),
            ("Shuttle Services Boats and Ferries", "Transportation"),
            ("Going out in a Car Moving in a car", "Transportation"),

            ("Payment to University Tuition", "Education"),
            ("College Textbooks", "Education"),
            ("Language School Enrollment", "Education"),
            ("Education Software Engineering Subscription", "Education"),
            ("Educational Business Workshop Registration", "Education"),
            ("Student Loan Repayment", "Education"),
            ("School Supplies Purchase", "Education"),
            ("University Housing and Board Fee", "Education"),
            ("Online Course Enrollment", "Education"),
            ("Educational Conference Registration", "Education"),

            ("Online Clothing Retailer Purchase", "Clothing"),
            ("Mall Department Store Shopping", "Clothing"),
            ("Fashion Boutique Purchase", "Clothing"),
            ("Fit and Active Gear Sportswear Retailer", "Clothing"),
            ("Seasonal Clearance Sale Shopping", "Clothing"),
            ("Luxury Brand Fashion Boutique", "Clothing"),
            ("Family Clothing Apparel Store", "Clothing"),
            ("Footwear Shoe Retailer", "Clothing"),
            ("All Clothes: Socks, Underwear, Boxers, Bras Purchase", "Clothing"),
            ("Designer Shirts, Pants, Jeans", "Clothing"),

            ("Amazon Online Shopping", "Online Payments"),
            ("PayPal, Zelle Payment Transfer", "Online Payments"),
            ("Netflix, Prime Video, Hulu Online Video Streaming Subscription", "Online Payments"),
            ("eBay Auction Win", "Online Payments"),
            ("Uber Eats, Doordash, GrubHub Dinner Food Delivery", "Online Payments"),
            ("Google Play, iTunes Application Purchase", "Online Payments"),
            ("Apple App Store, Android Play Store Video Games", "Online Payments"),
            ("Spotify Premium, Soundcloud, Pandora Music Listening Subscription", "Online Payments"),
            ("CashApp Online Payment", "Online Payments"),
            ("Wells Fargo, Bank Of America, JP Morgan Chase Wire Transfer", "Online Payments"),

            ("Miscellaneous Home Cooking and Cleaning Supplies", "Miscellaneous"),
            ("Handy Work Building Tools", "Miscellaneous"),
            ("Gas Station Fuel and Snacks", "Miscellaneous"),
            ("Books Purchase From Bookstore", "Miscellaneous"),
            ("Gift Shop For Travelling Tourists", "Miscellaneous"),
            ("New Tech Accessory, Laptop, Electronics Purchase", "Miscellaneous"),
            ("Antique Store For Furniture, Artwork, DIY Items, and Home Decor", "Miscellaneous"),
            ("Parking Fee", "Miscellaneous"),
            ("Gym Membership Renewal", "Miscellaneous"),
            ("Random Acts of Kindness Charity Donation", "Miscellaneous"),
        ]

        self.x, self.y = zip(*self.data)

        self.vectorizer = CountVectorizer()
        self.x_vectorized = self.vectorizer.fit_transform(self.x)

        self.classifier = MultinomialNB()
        self.classifier.fit(self.x_vectorized, self.y)

    def predict(self, statements):

        self.new_phrases_vectorized = self.vectorizer.transform(statements)

        predictions = self.classifier.predict(self.new_phrases_vectorized)

        return predictions