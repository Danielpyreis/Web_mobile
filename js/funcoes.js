function minhafuncao1(){
    alert('ALERTA');
    $('.btn-danger').empty().append('Novo nome');
    $('.btn-danger').css({
        color: '#00ff00',
        TextTranform: 'uppercase',
        width: '50%' 
    });

}

function minhafuncao2(){
    $('#area-mensagem').empty(); 

    var alunos= ['Aluno 01', 'Aluno 02', 'Aluno 03', 'Aluno 04'];
    $.each(alunos, function(index, value){
        $('#area-mensagem').append(value);
    });
}
