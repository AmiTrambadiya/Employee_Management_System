

//$(document).ready(function () {
//  $('#dtBasicExample').DataTable();
//  $('.dataTables_length').addClass('bs-select');
//});




function verifyPassword()
{
  var pw = document.getElementById("pswd").value;
  if(pw == "")
  {
     document.getElementById("message").innerHTML = "**Please fill the password";
     return false;
  }
  if(pw.length < 6)
  {
     document.getElementById("message").innerHTML = "**Password length must be 6 characters";
     return false;
  }
  if(pw.length > 6)
  {
     document.getElementById("message").innerHTML = "**Password length must be 6 characters";
     return false;
  }
  else
  {
        document.getElementById("message").innerHTML = "";
        return true;
  }
}

//function checkCity()
//{
//    var city = document.getElementById("chkcity").value;
//    if(city == "")
//    {
//        document.getElementById("chcity").innerHTML = "**Fill the city please!";
//        return false;
//    }
//    else
//    {
//        document.getElementById("chcity").innerHTML = "";
//        return true;
//    }
//}

function checkCity()
{
  var city = document.getElementById("chkcity").value;
  var a = /^[A-Za-z]{2,25}([A-Za-z]{2,25})?$/;
  if(a.test(city))
  {
    document.getElementById("chcity").innerHTML = "";
     return true;
  }
  if(city == "")
  {
     document.getElementById("chcity").innerHTML = "**Please fill the city";
     return false;
  }
  else
  {
        document.getElementById("chcity").innerHTML = "**Invalid city field";
        return false;
  }

}



function CheckIndianNumber()
{
  var mo = document.getElementById("mob").value;
  var a = /^[6789]\d{9}$/;
  if(a.test(mo))
  {
    document.getElementById("mobile").innerHTML = "";
     return true;
  }
  if(mo == "")
  {
     document.getElementById("mobile").innerHTML = "**Please fill the mobile number";
     return false;
  }
  if(mo.length < 10)
  {
     document.getElementById("mobile").innerHTML = "**Mobile number length must be 10 characters";
     return false;
  }
  if(mo.length > 10)
  {
     document.getElementById("mobile").innerHTML = "**Mobile number length must be 10 characters";
     return false;
  }
  else
  {
  document.getElementById("mobile").innerHTML = "**Your Mobile number is not valid";
  return false;
  }
}




function checkEmail(){
    var email = document.getElementById("chkemail").value;
    var a = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,63}$/;
  if(a.test(email))
  {
    document.getElementById("chemail").innerHTML = "";
     return true;
  }
  if(email == "")
  {
     document.getElementById("chemail").innerHTML = "**Please fill the email";
     return false;
  }
  else
  {
  document.getElementById("chemail").innerHTML = "**Your email is not valid";
  return false;
  }
}




function isZipCode()
{
  var zipcode = document.getElementById("zipCode1").value;
  var a = /^[0-9]{6}$/;
  if(a.test(zipcode))
  {
    document.getElementById("zip").innerHTML = "";
     return true;
  }
  if(zipcode == "")
  {
     document.getElementById("zip").innerHTML = "**Please fill the zipcode";
     return false;
  }
  if(zipcode.length < 6)
  {
     document.getElementById("zip").innerHTML = "**Zipcode length must be 6 characters";
     return false;
  }
  if(zipcode.length > 6)
  {
     document.getElementById("zip").innerHTML = "**Zipcode length must be 6 characters";
     return false;
  }
  else
  {
  document.getElementById("zip").innerHTML = "**Your Zipcode is not valid";
  return false;
  }
}

function bithDateValidate()
{
	var userinput = document.getElementById("birthDate").value;
    var dob = new Date(userinput);
    if(userinput==null || userinput=='')
    {
        document.getElementById("date").innerHTML = "Choose a date please!";
        return false;
    }
    else
    {
        var month_diff = Date.now() - dob.getTime();
        var age_dt = new Date(month_diff);
        var year = age_dt.getUTCFullYear();
        var age = Math.abs(year - 1970);
        if (age < 18)
        {
            document.getElementById("date").innerHTML = "Age should be more than 18 years. Please enter a valid Date of Birth";
            return false;
        }
        if (age > 50)
        {
            document.getElementById("date").innerHTML = "Age should be less than 50 years. Please enter a valid Date of Birth";
            return false;
        }
        else
        {
            document.getElementById("date").innerHTML = "";
            return true;
        }
    }
}


var male = document.getElementById("male");
var female = document.getElementById("female");
var checked = document.getElementById("gender").innerHTML;
if(checked == "Male")
{
    male.click()
}
else if(checked == "Female")
{
    female.click()
}
else
{}



function checkFirstname()
{
  var firstname = document.getElementById("chkfirstnm").value;
  var a = /^[A-Za-z]{2,25}([A-Za-z]{2,25})?$/;
  if(a.test(firstname))
  {
    document.getElementById("chfirstnm").innerHTML = "";
     return true;
  }
  if(firstname == "")
  {
     document.getElementById("chfirstnm").innerHTML = "**Please fill the first name";
     return false;
  }
  else
  {
        document.getElementById("chfirstnm").innerHTML = "**Invalid first name";
        return false;
  }

}
//function checkFirstname()
//{
//    var firstname = document.getElementById("chkfirstnm").value;
//    if(firstname == "")
//    {
//        document.getElementById("chfirstnm").innerHTML = "**Fill the first name please!";
//        return false;
//    }
//    else
//    {
//        document.getElementById("chfirstnm").innerHTML = "";
//        return true;
//    }
//}



function checkconpw()
{
    var confirmpw = document.getElementById("chkconpw").value;
    if(confirmpw == "")
    {
        document.getElementById("chconpw").innerHTML = "**Please fill the confirm password";
        return false;
    }
    else
    {
        document.getElementById("chconpw").innerHTML = "";
        return true;
    }
}

function checkLastname()
{
  var lastname = document.getElementById("chklastnm").value;
  var a = /^[A-Za-z]{2,25}([A-Za-z]{2,25})?$/;
  if(a.test(lastname))
  {
    document.getElementById("chlastnm").innerHTML = "";
     return true;
  }
  if(lastname == "")
  {
     document.getElementById("chlastnm").innerHTML = "**Please fill the last name";
     return false;
  }
  else
  {
        document.getElementById("chlastnm").innerHTML = "**Invalid last name";
        return false;
  }

}

//function checkLastname()
//{
//    var lastname = document.getElementById("chklastnm").value;
//    if(lastname == "")
//    {
//        document.getElementById("chlastnm").innerHTML = "**Fill the last name please!";
//        return false;
//    }
//    else
//    {
//        document.getElementById("chlastnm").innerHTML = "";
//        return true;
//    }
//}
//




//function checkUsername()
//{
//    var username = document.getElementById("chkusernm").value;
//    if(username == "")
//    {
//        document.getElementById("chusernm").innerHTML = "**Please fill the username";
//        return false;
//    }
//    else
//    {
//        document.getElementById("chusernm").innerHTML = "";
//        return true;
//    }
//}

function checkUsername()
{
  var username = document.getElementById("chkusernm").value;
  var a = /^[A-Za-z][A-Za-z0-9_]{4,29}$/;
  if(a.test(username))
  {
    document.getElementById("chusernm").innerHTML = "";
     return true;
  }
  if(username == "")
  {
     document.getElementById("chusernm").innerHTML = "**Please fill the username";
     return false;
  }
  else
  {
        document.getElementById("chusernm").innerHTML = "**Invalid username";
        return false;
  }

}


function checkAddress()
{
    var address = document.getElementById("chkaddress").value;
    if(address == "")
    {
        document.getElementById("chaddress").innerHTML = "**Please fill the address";
        return false;
    }
    else
    {
        document.getElementById("chaddress").innerHTML = "";
        return true;
    }
}


function checkState()
{
    var state = document.getElementById("chkstate").value;
    if(state == "")
    {
        document.getElementById("chstate").innerHTML = "**Please choose the state";
        return false;
    }
    else
    {
        document.getElementById("chstate").innerHTML = "";
        return true;
    }
}

function checkPro()
{
    var fileInput =  document.getElementById('file');
    var filePath = fileInput.value;
    var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
    if(filePath == "")
    {
        document.getElementById("chpro").innerHTML = "**Please choose a Image";
        return false;
    }
    if (!allowedExtensions.exec(filePath))
    {
        document.getElementById("chpro").innerHTML = "**Invalid format";
        fileInput.value = '';
        return false;
    }
    
    else
    {
        document.getElementById("chpro").innerHTML = "";
        return true;
    }

}




function checkPdf()
{
    var fileInput =  document.getElementById('pdf');
    var filePath = fileInput.value;
    var allowedExtensions = /(\.pdf)$/i;
    if(filePath == "")
    {
        document.getElementById("chpdf").innerHTML = "**Please choose a birth certificate";
        return false;
    }
    if (!allowedExtensions.exec(filePath))
    {
        document.getElementById("chpdf").innerHTML = "**Invalid format";
        fileInput.value = '';
        return false;
    }
    if (fileInput.files[0].size >= 20971520)
    {
         document.getElementById("chpdf").innerHTML = "**File size should be less than or Equal to 20 MB";
    }
    else
    {
        document.getElementById("chpdf").innerHTML = "";
        return true;
    }

}


function upload(){
  var imgcanvas = document.getElementById("canv1");
  var fileinput = document.getElementById("finput");
  var image = new SimpleImage(fileinput);
  image.drawTo(imgcanvas);
}


//function checkState()
//{
//  var state = document.getElementById("chkstate").value;
//  var a = /^[A-Za-z]{2,25}([A-Za-z]{2,25})?$/;
//  if(a.test(state))
//  {
//    document.getElementById("chstate").innerHTML = "";
//     return true;
//  }
//  if(state == "")
//  {
//     document.getElementById("chstate").innerHTML = "**Please fill the state";
//     return false;
//  }
//  else
//  {
//        document.getElementById("chstate").innerHTML = "**Invalid state field";
//        return false;
//  }
//
//}









//function showAlert()
//{
//alert('Login successfully');
//}
//
//function updateAlert()
//{
//alert('Updated Successfully');
//}
//
//function userAdd()
//{
//alert('User Added Successfully');
//}
