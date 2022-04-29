list1 = [1, 2, 3]

console.log(list1);

list1 = [...list1, 4] // 스프레드 연산자
// 포문을 걸면서 리스트에 다시 넣는다.
// 포문 뿌리면서 4를 append함
console.log(list1);

let user = {
    id: 1,
    username: "cos"
}

let user2 = { ...user };
console.log(user2);

user = {...user, id:2} // 뿌리고 부분 변경
console.log(user);
// 키값이 같으면 가능하다. 키값이 500개였을 때 부분 변경이 가능하다.

let users = [
    {
        id: 1,
        username: "cos"
    },
    {
        id: 2,
        username: "ssar"
    }
];

let updateUsers = [...users, { id: 2, uesrname: "hello" }];

console.log(updateUsers);