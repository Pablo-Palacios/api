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
    get_task





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
    return requests.get(HTTP + f"/get-task{task_id}")