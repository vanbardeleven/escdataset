import pandas as pd
import gender_guesser.detector as gender

def add_identity_and_gender(column_name, country_column, names_list):
    # Initialize gender detector
    d = gender.Detector()
    
    # Read the contestants CSV file into a DataFrame
    df = pd.read_csv('contestants.csv')
    
    # Print column names for debugging
    print("Columns in DataFrame:", df.columns)
    
    # Strip whitespace from column names
    df.columns = df.columns.str.strip()
    
    # Check if the DataFrame is empty
    if df.empty:
        print("The DataFrame is empty. Check if the CSV file is correctly populated.")
        return
    
    def get_status(row):
        # Extract the name and country from the row
        name = row[column_name]
        country = row[country_column]
        
        # Check if the combination of name and country is in the special list
        if (name, country) in names_list:
            return 'othere'  # Returns 'othere' for matched name-country pairs
        else:
            # Get the first name (assuming it's the first word)
            first_name = name.split()[0]
            # Return gender prediction
            return d.get_gender(first_name)
    
    # Create the gender column with either 'othere' or the gender prediction
    df['gender'] = df.apply(get_status, axis=1)
    
    # Save the modified DataFrame back to the same CSV file
    df.to_csv('contestants.csv', index=False)
    print('Updated contestants.csv with identity/gender entries')

# List of (name, country) pairs to check
names_list = [
    ("Dany Dauberson", "France"), ("Bob Benny", "Belgium"), ("Bob Benny", "Belgium"),
    ("Jean-Claude Pascal", "Luxembourg"), ("Kathy Kirby", "United Kingdom"),
    ("Ronnie Tober", "Netherlands"), ("Patrick Juvet", "Switzerland"),
    ("Jürgen Marcus", "Luxembourg"), ("Jean-Claude Pascal", "Luxembourg"),
    ("Gerard Joling", "Netherlands"), ("Dina", "Portugal"),
    ("Christer Björkman", "Sweden"), ("Sara", "Portugal"), ("Paul Oscar", "Iceland"),
    ("Gabriel Forss", "Sweden"), ("Katrina Leskanich", "United Kingdom"),
    ("Dana International", "Israel"), ("Michelle", "Netherlands"), ("Piasek", "Poland"),
    ("Kim Kärnfalk", "Sweden"), ("Sarit Hadad", "Israel"),
    ("Julia Volkova", "Russia"), ("Deen", "Bosnia and Herzegovina"),
    ("Tomas Thordarson", "Denmark"), ("Jari Sillanpää", "Finland"),
    ("Jonatan Cerrada", "France"), ("Knut Anders Sørum", "Norway"),
    ("Donna McCaul", "Ireland"), ("Brian Kennedy", "Ireland"),
    ("Andreas Lundstedt", "Switzerland"), ("Marija Šerifović", "Serbia"),
    ("Olga Seryabkina and Elena Temnikova", "Russia"), ("Javi Soleil", "Spain"),
    ("Ola Salo", "Sweden"), ("David Ducasse", "United Kingdom"),
    ("Lucy Diakovska", "Germany"), ("Friðrik Ómar", "Iceland"), 
    ("Oscar Loya", "Germany"), ("Gordon Heuckeroth", "Netherlands"),
    ("Harel Skaat", "Israel"), ("Michael von der Heide", "Switzerland"),
    ("Dana International", "Israel"), ("Glen Vella", "Malta"),
    ("Duncan James and Lee Ryan", "United Kingdom"), ("Tooji", "Norway"),
    ("Loreen", "Sweden"), ("Ryan Dolan", "Ireland"), ("Conchita Wurst", "Austria"),
    ("Axel Hirsoux", "Belgium"), ("Amber", "Malta"),
    ("Deen", "Bosnia and Herzegovina"), ("Nina Kraljić", "Croatia"),
    ("Johannes Nymark", "Denmark"), ("Jamie-Lee", "Germany"),
    ("Hovi Star", "Israel"), ("Douwe Bob", "Netherlands"),
    ("Michal Szpak", "Poland"), ("Rykka", "Switzerland"),
    ("Imri Ziv", "Israel"), ("Slavko Kalezić", "Montenegro"),
    ("Salvador Sobral", "Portugal"), ("Saara Aalto", "Finland"),
    ("Mélovin", "Ukraine"), ("Bilal Hassani", "France"),
    ("Duncan Laurence", "Netherlands"), ("Tom Hugo", "Norway"),
    ("Montaigne", "Australia"), ("Jendrik", "Germany"),
    ("Lesley Roy", "Ireland"), ("Victoria De Angelis and Ethan Torchio", "Italy"),
    ("Jeangu Macrooy", "Netherlands"), ("Vasil", "North Macedonia"),
    ("Roxen", "Romania"), ("Blas Cantó", "Spain"),
    ("Sheldon Riley", "Australia"), ("Elín Eyþórsdóttir", "Iceland"),
    ("Michael Ben David", "Israel"), ("Andrei Ursu", "Romania"),
    ("Gustaph", "Belgium"), ("Alessandra Mele", "Norway"),
    ("Luke Black", "Serbia"), ("Loreen", "Sweden"),
    ("Zaachariaha Fielding and Michael Ross", "Australia"), ("Mustii", "Belgium"),
    ("Aiko", "Czech Republic"), ("Saba", "Denmark"),
    ("Bambie Thug", "Ireland"), ("Silvester Belt", "Lithuania"),
    ("Kenzy Loevett and Kat Almagro", "San Marino"), ("Nemo", "Switzerland"),
    ("Olly Alexander", "United Kingdom")
]

# Call the function with 'performer' as the column name and 'to_country' as the country column
add_identity_and_gender('performer', 'to_country', names_list)
