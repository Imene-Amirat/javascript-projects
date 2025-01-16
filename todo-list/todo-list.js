const todoList = [];

renderTodoList();

function renderTodoList(){
    let todoListhtml ='';

    todoList.forEach((todoObj,index) => {
    const html = `
        <div>${todoObj.name}</div>
        <div>${todoObj.date}</div>
        <button class="delete-btn js-delete-btn">Delete</button>
    ` ;
    todoListhtml += html;
    });
    document.querySelector('.js-todo-list').innerHTML = todoListhtml ;

    document.querySelectorAll('.js-delete-btn').forEach((deleteButtonElement, index) => {
    deleteButtonElement.addEventListener('click', () => {
        deletetodo(index);
    })
    })

}


document.querySelector('.js-add').addEventListener('click', () => {
    add()
}) 

function add(){
    const name = document.querySelector('.js-todo').value;
    const date = document.querySelector('.js-date').value;

    todoList.push({name, date});
    document.querySelector('.js-todo').value = '';
    document.querySelector('.js-date').value = '';
    renderTodoList();
    
}

function deletetodo(i){
    todoList.splice(i,1);
    renderTodoList();
    
}