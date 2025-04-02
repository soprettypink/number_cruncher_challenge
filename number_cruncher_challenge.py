#number_cruncher.py
def process_numbers(input_filename = "numbers.txt"):
    total = 0.0 #adds all numbers together
    count = 0 #holds how many numbers are listed
    min_value = None #holds the minimum value; no minimum value has been found yet
    max_value = None #holds the maximum value; no maximum value has been found yet
    average = 0.0 #holds the average of the list of numbers
    numbers = [] #stores numbers to be calculated later

    try:
        with open("numbers.txt", "r") as infile: #opens and reads the input file
            for line in infile: #loops over each line of file
                stripped_line = line.strip() #removes whitespace

                if not stripped_line: #skips empty liines
                    continue

                try:
                    value = float(stripped_line)
                    numbers.append(value) #adds a number to the list
                    #total += value
                    #count += 1
                    #if min_value == None or value < min_value:
                    #    min_value = value
                    #if max_value == None or value > max_value:
                    #    max_value = value
                    #if count != 0:
                    #    average = total / count #calculates the average
                    #else:
                    #    average = 0 #this avoids an error message
                
                except ValueError: #prints error messages when stripped lines cannot be converted to a number
                    error_message = f"Error: 'Could not convert '{stripped_line}' to a number. Skipping."
                    print(error_message)
                    try:
                        with open("error.txt", "a") as error_file:
                            error_file.write(error_message)
                    except IOError as log_e:
                        print("Error: Could not write to error_log.txt")
    
        count = len(numbers) 
        if count > 0:
            total = sum(numbers)
            averagev= total / count
            min_value = min(numbers)
            max_value = max(numbers)
        #if count has the value of 0, initial values remain correct

        try:
            with open("report.txt", "w") as outfile:
                outfile.write(f"Report \n")
                outfile.write(f"------\n")
                outfile.write(f"Count: {count} \n")
                outfile.write(f"Sum: {total} \n")
                if count > 0:
                    outfile.write(f"Average: {average} \n")
                    outfile.write(f"Minimum: {min_value} \n")
                    outfile.write(f"Maximum: {max_value} \n")
                else:
                    outfile.write("Average: N/A\n")
                    outfile.write("Minimum: N?A\n")
                    outfile.write("Maximum: N/A\n")
            print("File processing complete!")
        except IOError as report_e:
            print("Error: Writing report file 'report.txt' was unsuccessful.")

    except FileNotFoundError:
        print("Error: 'numbers.txt' could not be found.")
        return None #when the file fails to open, this result is displayed
    except IOError as reas_e:
        print(f"Error: Could not read 'numbers.txt'.")
        return None #when the file fails to be read, this result is displayed
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        try:
            with open("error_log.txt", "a") as error_file: #adds the log into error_log.txt
                error_file.write(f"Unexpected error: {e}\n")
        except IOError:
            pass #ignores logging failure
    finally:
        print("File processing complete!")
    
    return count, average, total, min_value, max_value

if __name__ == "__main__":
    results = process_numbers()

    if results: #prints the results if the processing is successful
        print("\n---- Summary ----")
        count, total, average, min_val, max_val = results
        print(f"Count: {count}")
        print(f"Sum: {total}")
        if count > 0:
            print(f"Average: {average}")
            print(f"Minimum:{min_val}")
            print(f"Maximum: {max_val}")
        else:
            print("No numbers found in the file.")
            print("Check 'report.txt' for the report and 'error_log' for errors.")
    else:
        print("\nProcess could not be completed.")