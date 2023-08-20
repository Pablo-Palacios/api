import requests
import uuid

HTTP = "https://todo.pixegami.io/"


"                             Testeo de la API                          "

def test_can_conex_api():
    conex_api = requests.get(HTTP)
    assert conex_api.status_code == 200

    

def test_can_create_task():
    task = playload_task()
    create_task_response = create_task(task)
    assert create_task_response.status_code == 200




def test_can_get_task():
    task = playload_task()
    create_task_response = create_task(task)
    assert create_task_response.status_code == 200

    data = create_task_response.json()

    #print(data)
    task_id = data ["task"]["task_id"]
    get_task_reponse = get_task(task_id)
    assert get_task_reponse.status_code == 200 


def test_can_update_task():
    task = playload_task()
    create_task_response = create_task(task)
    data = create_task_response.json()
    task_id = data ["task"]["task_id"]
    assert create_task_response.status_code == 200

    new_playload = {
                    "content": "my content update",
                    "user_id": task["user_id"],
                    "task_id": task_id,
                    "is_done": True
                                        }
    
    update_task_response = update_task(new_playload)
    print(new_playload)
    assert update_task_response.status_code == 200 


def test_can_take_list_tasks():
    n = 5
    task = playload_task()
    for _ in range(n):
        create_task_response = create_task(task)
        assert create_task_response.status_code == 200

    user_id = task["user_id"]
    list_tasks_response = list_tasks(user_id)
    assert list_tasks_response.status_code == 200 

    data = list_tasks_response.json()
    print(data)

    tasks = data["tasks"]
    assert len(tasks) == n 














    






#######################################################

def playload_task():
    user_id = f"my_user_{uuid.uuid4().hex}"
    content = f"content_{uuid.uuid4().hex}"
    #task_id = f"task_id_{uuid.uuid4().hex}"
    return {
            "content": content,
            "user_id": user_id,
            #"task_id": task_id,
            "is_done": False
                                    }



def create_task(playload):
    return requests.put(HTTP + "/create-task", json= playload)

def get_task(task_id):
    return requests.get(HTTP + f"/get-task/{task_id}")



def update_task(playload):
    return requests.put(HTTP + "/update-task", json= playload)


def list_tasks(user_id):
    return requests.get(HTTP + f"/list-tasks/{user_id}")