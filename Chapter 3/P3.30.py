"""
••• P3.30 French country names are feminine when they end with the letter e, masculine otherwise, except for the following which are masculine even though they end with e:
• le Belize
• le Cambodge
• le Mexique
• le Mozambique
• le Zaïre
• le Zimbabwe
Write a program that readsthe French name of a country and addsthe article: le for 
masculine or la for feminine, such as le Canada or la Belgique.
However, if the country name starts with a vowel, use l’; for example, l’Afghanistan. 
For the following plural country names, use les:
• les Etats-Unis
• les Pays-Bas
"""
def main():
    # Dictionary of exceptions where country names are masculine
    masculine_exceptions = {"Belize", "Cambodge", "Mexique", "Mozambique", "Zaïre", "Zimbabwe"}

    # Get user input for the country name
    country_name = input("Enter the French name of a country: ").strip().capitalize()

    # Determine the appropriate article based on the rules
    article = ""

    if country_name in masculine_exceptions:
        article = "le"
    elif country_name.endswith("e"):
        article = "la"
    elif country_name.startswith(("A", "E", "I", "O", "U")):
        article = "l'"
    else:
        article = "le"

    # Print the formatted country name with the article
    print(f"{article} {country_name}")

if __name__ == "__main__":
    main()

