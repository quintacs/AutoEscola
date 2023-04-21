
var url = "http://127.0.0.1:5000";

function loadAlunos(){
    var urlLocal = url+"/ListaAlunos";

    var table = "<div class='table-responsive'>";
        table+="<table class='table table-hover'>   ";       
        table+="    <thead>				";
        table+="      <tr>";
        table+="        <th></th> ";
        table+="        <th></th>";
        table+="        <th></th>";
        table+="        <th></th>";
        table+="        <th></th>";
        table+="        <th><div class='adiciona-tabela' onclick=\"javascript:alteraDisplay('form-aluno','block');\" > + </div></th>";
        table+="        <th><div class='fechar-tabela' onclick=\"javascript:alteraDisplay('lista','none'); \" > x </div></th>";
        table+="      </tr>";    
        table+="      <tr>";
        table+="        <th>#</th> ";
        table+="        <th>Nome</th>";
        table+="        <th>Idade</th>";
        table+="        <th>Endereco</th>";
        table+="        <th>Telefone</th>";
        table+="        <th>Data de Nascimento</th>";
        table+="        <th>Matricula</th>";
        table+="      </tr>";
        table+="    </thead>";
        table+="    <tbody>";
    
    fetch(urlLocal, {
        method: 'get',
      })
        .then((response) => response.json())
        .then((data) => {
            //alert(data.alunos[0].nome);
                
            var alunos = data.alunos;

            for(index = 0; index < alunos.length; index++){
                table+="      <tr>";
                table+="<td> <div class='glyphicon glyphicon-edit' onclick=\"javascript:loadAluno('"+alunos[index].id+"');\" >  </div></td>";
                table+="<td>"+alunos[index].nome            +"</td>";
                table+="<td>"+alunos[index].idade           +"</td>";
                table+="<td>"+alunos[index].endereco        +"</td>";
                table+="<td>"+alunos[index].telefone        +"</td>";
                table+="<td>"+alunos[index].data_nascimento +"</td>";
                table+="<td>"+alunos[index].matricula       +"</td>";
                table+="      </tr>";
            }

            table+="    </tbody>";
            table+="  </table>";
            table+="  </div>";
           // alert(table);
            document.getElementById("lista").innerHTML = table;
        })
        .catch((error) => {
          console.error('Error:', error);
        });
}

function loadAluno(id){
    var urlLocal = url+"/BuscaAluno?id="+id;

    
    fetch(urlLocal, {
        method: 'get',
      })
        .then((response) => response.json())
        .then((data) => {
            //alert(data.alunos[0].nome);
                
            var aluno = data;

            //alert(aluno.data_nascimento);
            document.getElementById("id_aluno").value = aluno.id;
            document.getElementById("nome_aluno").value = aluno.nome;
            document.getElementById("idade_aluno").value = aluno.idade;
            document.getElementById("endereco_aluno").value = aluno.endereco;
            document.getElementById("telefone_aluno").value = aluno.telefone;
            document.getElementById("data_nascimento_aluno").value = aluno.data_nascimento;
            document.getElementById("matricula_aluno").value = aluno.matricula

            alteraDisplay('form-aluno','block');
        })
        .catch((error) => {
          console.error('Error:', error);
        });
}


function loadInstrutores(){
    var urlLocal = url+"/ListaInstrutores";

    var table = "<div class='table-responsive'>";
        table+="<table class='table table-hover'>   ";       
        table+="    <thead>				";
        table+="      <tr>";
        table+="        <th></th> ";
        table+="        <th></th>";
        table+="        <th></th>";
        table+="        <th></th>";
        table+="        <th></th>";
        table+="        <th><div class='adiciona-tabela' onclick=\"javascript:alteraDisplay('form-instrutor','block'); \" > + </div></th>";
        table+="        <th><div class='fechar-tabela' onclick=\"javascript:alteraDisplay('lista','none'); \" > x </div></th>";
        table+="      </tr>";        
        table+="      <tr>";
        table+="        <th>#</th> ";
        table+="        <th>Nome</th>";
        table+="        <th>Idade</th>";
        table+="        <th>Endereco</th>";
        table+="        <th>Telefone</th>";
        table+="        <th>Data de Nascimento</th>";
        table+="        <th>Agenda</th>";
        table+="      </tr>";
        table+="    </thead>";
        table+="    <tbody>";
    
    fetch(urlLocal, {
        method: 'get',
      })
        .then((response) => response.json())
        .then((data) => {
            //alert(data.alunos[0].nome);
                
            var instrutores = data.instrutores;

            for(index = 0; index < instrutores.length; index++){
                table+="      <tr>";
                table+="<td> <div class='glyphicon glyphicon-edit' onclick=\"javascript:loadInstrutor('"+instrutores[index].id+"');\" >  </div></td>";
                table+="<td>"+instrutores[index].nome            +"</td>";
                table+="<td>"+instrutores[index].idade           +"</td>";
                table+="<td>"+instrutores[index].endereco        +"</td>";
                table+="<td>"+instrutores[index].telefone        +"</td>";
                table+="<td>"+instrutores[index].data_nascimento +"</td>";
                table+="<td>"+instrutores[index].agenda          +"</td>";
                table+="      </tr>";
            }

            table+="    </tbody>";
            table+="  </table>";
            table+="  </div>";
           // alert(table);
            document.getElementById("lista").innerHTML = table;
        })
        .catch((error) => {
          console.error('Error:', error);
        });
}


function loadInstrutor(id){

    var urlLocal = url+"/BuscaInstrutor?id="+id;
    
    fetch(urlLocal, {
        method: 'get',
      })
        .then((response) => response.json())
        .then((data) => {
            //alert(data.alunos[0].nome);
                
            var instrutor = data;

            //alert(aluno.data_nascimento);
            document.getElementById("id_instrutor").value = instrutor.id;
            document.getElementById("nome_instrutor").value = instrutor.nome;
            document.getElementById("idade_instrutor").value = instrutor.idade;
            document.getElementById("endereco_instrutor").value = instrutor.endereco;
            document.getElementById("telefone_instrutor").value = instrutor.telefone;
            document.getElementById("data_nascimento_instrutor").value = instrutor.data_nascimento;
            document.getElementById("agenda_instrutor").value = instrutor.agenda

            alteraDisplay('form-instrutor','block');
        })
        .catch((error) => {
          console.error('Error:', error);
        });
}


/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (urlImput, body) => {
    
   /* alert("url: "+urlImput+
        "\n body: "+body);*/
  
    var urlLocal = url + urlImput;
    
   /* alert("url: "+urlImput+
         "\n body: "+body
         +"\n  urlLocal: "+urlLocal);*/

    fetch(urlLocal, {
      method: 'post',
      body: body
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error('Error:', error);
      });
}

const putItem = async (urlImput, body) => {
    
    /* alert("url: "+urlImput+
         "\n body: "+body);*/
   
     var urlLocal = url + urlImput;
     
    /* alert("url: "+urlImput+
          "\n body: "+body
          +"\n  urlLocal: "+urlLocal);*/
 
     fetch(urlLocal, {
       method: 'put',
       body: body
     })
       .then((response) => response.json())
       .catch((error) => {
         console.error('Error:', error);
       });
 }
 
  
/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newInstrutor = () => {

    var nome			= document.getElementById("nome_instrutor").value;
    var idade			= document.getElementById("idade_instrutor").value;
    var endereco		= document.getElementById("endereco_instrutor").value;
    var telefone		= document.getElementById("telefone_instrutor").value;
    var data_nascimento = document.getElementById("data_nascimento_instrutor").value;
    var agenda		    = document.getElementById("agenda_instrutor").value;

    /*alert(nome		+" \n"+
        idade			+" \n"+
        endereco		+" \n"+
        telefone		+" \n"+
        data_nascimento +"\n"+  
        agenda		);*/

    const formData = new FormData();
	formData.append('nome',nome				);
    formData.append('idade',idade			    );
    formData.append('endereco',endereco			);
    formData.append('telefone',telefone			);
    formData.append('data_nascimento',data_nascimento	);
    formData.append('agenda',agenda   		    );
  
   // alert("formData: "+formData);

    var id = document.getElementById("id_instrutor").value;
    if(id == 0 ){
        postItem('/AdicionaInstrutor', formData);
    }else{
        putItem('/AtualizaInstrutor/'+id,formData);
    }

    loadInstrutores();

    /*if (inputProduct === '') {
      alert("Escreva o nome de um item!");
    } else if (isNaN(inputQuantity) || isNaN(inputPrice)) {
      alert("Quantidade e valor precisam ser números!");
    } else {
      //insertList(inputProduct, inputQuantity, inputPrice)
      postItem('/AdicionaInstrutor', formData)
      alert("Instrutor adicionado!")
    }*/
  }

  
/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newAluno = () => {

    var nome			= document.getElementById("nome_aluno").value;
    var idade			= document.getElementById("idade_aluno").value;
    var endereco		= document.getElementById("endereco_aluno").value;
    var telefone		= document.getElementById("telefone_aluno").value;
    var data_nascimento = document.getElementById("data_nascimento_aluno").value;
    var matricula	    = document.getElementById("matricula_aluno").value;
    
   /* alert(nome		+" \n"+
        idade			+" \n"+
        endereco		+" \n"+
        telefone		+" \n"+
        data_nascimento +"\n"+  
        matricula		);*/

    const formData = new FormData();
	formData.append('nome',nome				);
    formData.append('idade',idade			    );
    formData.append('endereco',endereco			);
    formData.append('telefone',telefone			);
    formData.append('data_nascimento',data_nascimento	);
    formData.append('matricula',matricula		    );
    
    //alert("formData: "+formData);
    var id = document.getElementById("id_aluno").value;
    if(id == 0 ){
        postItem('/AdicionaAluno',formData);
    }else{
        putItem('/AtualizaAluno/'+id,formData);
    }
    
    
    /*if (inputProduct === '') {
      alert("Escreva o nome do aluno!");
    } else if (isNaN(inputQuantity) || isNaN(inputPrice)) {
      alert("Quantidade e valor precisam ser números!");
    } else {
      //insertList(inputProduct, inputQuantity, inputPrice)
      postItem('/AdicionaAluno',formData)
      alert("Item adicionado!")
    }*/
  }
  

  

  function controleDisplay(myDIV) {
    var x = document.getElementById(myDIV);
    if (x.style.display === 'none') {
      x.style.display = 'block';
    } else {
      x.style.display = 'none';
    }
  }
  
  function alteraDisplay(myDIV,d) {
    var x = document.getElementById(myDIV);
    if (x.style.display === d) {
      x.style.display = d;
    } else {
      x.style.display = d;
    }
  }
  
  function loadForm(){
      //listaRelatorios();
      //alteraDisplay('lsStatusPrevisao','block');
      document.getElementById("id_aluno").value =  0;
      document.getElementById("id_instrutor").value =  0; 
      alteraDisplay('form-instrutor','none');
      alteraDisplay('form-aluno','none');
      alteraDisplay('lista','none');
      //controleDisplay('agendamentos');
  }

  function limpaAluno(){
    document.getElementById("id_aluno").value =  0;
    document.getElementById("nome_aluno").value = "";
    document.getElementById("idade_aluno").value = "";
    document.getElementById("endereco_aluno").value = "";
    document.getElementById("telefone_aluno").value = "";
    document.getElementById("data_nascimento_aluno").value = "";
    document.getElementById("matricula_aluno").value  = "";
  }

  function limpaInstrutor(){
    document.getElementById("id_instrutor").value =  0; 
    document.getElementById("nome_instrutor").value = "";
    document.getElementById("idade_instrutor").value = "";
    document.getElementById("endereco_instrutor").value = "";
    document.getElementById("telefone_instrutor").value = "";
    document.getElementById("data_nascimento_instrutor").value = "";
    document.getElementById("agenda_instrutor").value = "";
  }
