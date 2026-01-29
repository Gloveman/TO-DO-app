import streamlit as st

class Todo:
    def __init__(self, task:str, is_done:bool = False):
        self.__task = task
        self.__done = is_done

    def get_task(self):
        return self.__task

    def get_done(self):
        return self.__done
    def set_done(self,value):
        self.__done = value
    # def __str__(self):
    #     return f'Task: {self.__task}, Done: {self.__done}'

    # 객체가 container 안에 있을 때 '컨테이너 자체'를 출력하게 되면 표시되는 값
    # str이 정의되어 있지 않으면 이것이 실행됨
    def __repr__(self):
        return f'Task: {self.__task}, Done: {self.__done}'
        #repr은 eval()로 다시 객체로 바꿀 수 있는 문자열 형태로 작성하는게 원칙
        #eval(repr(obj)) == obj
        #return f'Todo(task= "{self.__task}", is_done= "{self.__done}")'

# print(Todo('숙제'))
# print(Todo('기상', True))
# todo1 = Todo('라면먹기')
# print(todo1)
# todo2 = repr(todo1)
# print(todo1 is eval(todo2))
# print(todo1 == eval(todo2))#repr로부터 새로운 객체 생성 가능(기존 객체와 다른 주소)



#일정 추가
def add_todo():
    todo = Todo(st.session_state.new_task)
    st.session_state.todos.append(todo)
    st.session_state.new_task = ""

def toggle_done(idx):
    todo = st.session_state.todos[idx]
    todo.set_done(not todo.get_done())
#일정 담는 todos 리스트
if 'todos' not in st.session_state:
    st.session_state.todos = []

st.title('TO-DO List')

# key 속성을 설정하면 사용자가 입력한 값이 key라는 이름으로 session state에 저장된다.
# 이후 다시 렌더링 되었을때는 new_task의 값이 들어있다.
st.text_input('새로운 할일 추가', key='new_task',on_change = add_todo)

st.subheader('현재 일정 목록')
if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):
        #st.write(f'{i+1}번째 할일 => {todo}')
        col1, col2 = st.columns([0.1,0.9])
        # args는 무조건 tuple.
        col1.checkbox(f'{i+1}', value = todo.get_done(), on_change = toggle_done, args = (i,)) 
        col2.markdown(f'~~{todo.get_task()}~~' if todo.get_done() else todo.get_task())

else:
    st.info('할 일이 아직 없어요')

