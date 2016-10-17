
#***
#*  Dictionary Examples
#*  17 October 2016
#*  Melanie Cornelius, mseryn, melanie.e.cornelius@gmail.com
#*  
#*  Instructions:
#*      Make a dictionary to store people’s names by their zip codes. Have it
#*      take user inputs to collect this data.
#***

# Using Python's equivalent of main
if __name__ == "__main__":
    # Making the dictionary:
    zip_codes_to_names = {}

    # Making some storage variables
    name = None
    zip_code = None

    # Giving the user instructions:
    print("Enter the requested information, or enter 'q' as the name to quit.")

    # Collecting user inputs again
    name = input("Name: ")
    zip_code = input("Zip code: ")

    while name != 'q':

        # Ensuring the key already has an array associated with it - if not, 
        # make the array.
        if zip_code not in zip_codes_to_names:
            zip_codes_to_names[zip_code] = []

        # Adding the input name to the dictionary under the zip code
        zip_codes_to_names[zip_code].append(name)

        # Collecting user inputs again
        name = input("Name: ")
        zip_code = input("Zip code: ")

    # Now that the user is done, print the dictionary
    print(zip_codes_to_names)    
