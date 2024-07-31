import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)
            # print(test)
            return test
         
    except FileNotFoundError:
        return []
    
    
    
def save_data(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_video(videos):
    print("\n")
    print("*" * 70)
    if videos is not None:
        for index,video in enumerate(videos,start=1):
            print(f"{index}. Name : {video['name']}, Duration : {video['time']} \n")
    else:
        print("No videos are here")
        
        

def add_video(videos):
    name = input("Enter the video name : ")
    time  = input("Enter the video time : ")
    videos.append({'name':name,'time':time})
    save_data(videos)
    
    
def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter the video number to update : "))
    if 1 <= index <= len(videos):
        n_name = input("Enter the new video name : ")
        n_time = input("Enter the new video time : ")
        videos[index-1] = {'name':n_name,'time':n_time}
        save_data(videos)
    else:
        print("Invalid index selected.")
    


def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter the video to index deleted  : "))
    if 1 <= index <= len(videos):
        del videos[index -1]
        save_data(videos)
    else:
        print("Invaild video index selected.")




def main():
    videos  = load_data()
    while True:
        print("\n Youtube Manager || Chose your option.")
        print("\n1. List all Video.")
        print("2. Add youtube video.")
        print("3. Update yt video.")
        print("4. Delete Video.")
        print("5. Exit the app.")
        # print(videos)
        choice = int(input("Enter your choice : "))
        
        match choice:
            case 1:
                list_all_video(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _:
                print("Invalid choice.")
        






if __name__ == "__main__":
    main()