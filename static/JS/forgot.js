function repass (){
    $('#btnSubmitrepass').on('click',function(){
        $.ajax({
            url:'/user/list',
            type:  'get',
            dataType:  'json',
            success: function  (data) {
                var cus_id = data.cus_id
                var username = document.getElementById('username').value;
                var email = document.getElementById('email').value;
                var newpsw = document.getElementById('psw').value;
                var cpsw = document.getElementById('cpsw').value;
                    if (username == "" || email == "" || newpsw == ""|| cpsw == "") {
                        alert('Please fill all the details');
                    }
                   
                    else if (data == username) {
                        alert("user match");
                    }
                    else if (data == email) {
                        alert("email match");
                    }
                    else if (newpsw != cpsw) {
                        alert("password mismatch");
                    }else {
                        alert('บันทึกสำเร็จ');
                    }
            
            }
        })
    })
}
