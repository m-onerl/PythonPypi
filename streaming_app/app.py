from streaming.streaming_services import StreamingAvailability, DataProcessor

def main():
    api_key = '6f15df70bemshf21dbcbfe196f8cp155c96jsn3adbaed9ea15'
    streaming = StreamingAvailability(api_key)
    processor = DataProcessor()

    country = input("Please enter the country code (e.g., US, PL etc.): ").strip()

    if not country:
        print("Country is required.")
        return

    print("Please choose the search option:")
    print("1. Search by filters (type of show)")
    print("2. Search by title")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        print("Please choose the show type:")
        print("1. Movie")
        print("2. Series")
        show_choice = input("Enter the number of your choice: ").strip()

        if show_choice == '1':
            show_type = 'movie'
        elif show_choice == '2':
            show_type = 'series'
        else:
            print("Invalid choice. Please enter 1 or 2.")
            return

        result = streaming.search_shows_by_filters(country, show_type)

    elif choice == '2':
        title = input("Please enter the title: ").strip()
        result = streaming.search_shows_by_title(country, title)

    else:
        print("Invalid choice. Please enter 1 or 2.")
        return


    try:
        processed_data = processor.process_data(result)
    except ValueError as e:
        print(f"Error processing data: {e}")
        return

    for title, details in processed_data.items():
        print(f"Title: {title}")
        print(f"Overview: {details['overview']}")
        print(f"Release Year: {details['releaseYear']}")
        print(f"Genres: {', '.join(details['genres'])}")
        print(f"Directors: {', '.join(details['directors'])}")
        print(f"Cast: {', '.join(details['cast'])}")
        print(f"Rating: {details['rating']}")
        print()

if __name__ == "__main__":
    main()
