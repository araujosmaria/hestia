/**
 * Cadastro Form - Funcionalidades do formulário de cadastro
 * Inclui: preview de foto, validação de senha, máscaras de input e integração com ViaCEP
 */
(function() {
    document.addEventListener('DOMContentLoaded', () => {
        const fotoPerfil = document.getElementById('fotoPerfil');
        const previewContainer = document.getElementById('preview-foto-container');
        const previewFoto = document.getElementById('preview-foto');
        const form = document.getElementById('formCliente');

        // Se não encontrar o formulário, não executa
        if (!form) return;

        // Preview da foto de perfil
        setupPhotoPreview();

        // Validação de senha
        setupPasswordValidation(form);

        // Máscaras de input
        setupInputMasks();

        // Integração ViaCEP
        setupCEPLookup();
    });

    /**
     * Configura o preview da foto de perfil
     */
    function setupPhotoPreview() {
        const fotoPerfil = document.getElementById('fotoPerfil');
        const previewContainer = document.getElementById('preview-foto-container');
        const previewFoto = document.getElementById('preview-foto');

        if (!fotoPerfil) return;

        fotoPerfil.addEventListener('change', (event) => {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    previewFoto.src = e.target.result;
                    previewContainer.style.display = 'flex'; // Usar flex para centralizar
                };
                reader.readAsDataURL(file);
            } else {
                previewContainer.style.display = 'none';
            }
        });
    }

    /**
     * Configura a validação de senha no submit do formulário
     * @param {HTMLFormElement} form - O formulário a ser validado
     */
    function setupPasswordValidation(form) {
        form.addEventListener('submit', (e) => {
            const senha = document.getElementById('senha').value;
            const confirmarSenha = document.getElementById('confirmarSenha').value;

            if (senha.length < 8) {
                e.preventDefault();
                alert('A senha deve ter pelo menos 8 caracteres.');
                return;
            }
            if (senha !== confirmarSenha) {
                e.preventDefault();
                alert('As senhas não coincidem!');
            }
        });
    }

    /**
     * Configura as máscaras de input para telefone, CPF e CEP
     */
    function setupInputMasks() {
        // Máscara de telefone
        const telefoneInput = document.getElementById('telefone');
        if (telefoneInput) {
            telefoneInput.addEventListener('input', (e) => {
                let value = e.target.value.replace(/\D/g, ''); // Remove tudo que não é dígito
                if (value.length > 10) {
                    value = value.replace(/^(\d{2})(\d{5})(\d{4}).*/, '($1) $2-$3');
                } else if (value.length > 6) {
                    value = value.replace(/^(\d{2})(\d{4})(\d{0,4}).*/, '($1) $2-$3');
                } else if (value.length > 2) {
                    value = value.replace(/^(\d{2})(\d{0,5}).*/, '($1) $2');
                } else {
                    value = value.replace(/^(\d*)/, '($1');
                }
                e.target.value = value;
            });
        }

        // Máscara de CPF
        const cpfInput = document.getElementById('cpf');
        if (cpfInput) {
            cpfInput.addEventListener('input', (e) => {
                let value = e.target.value.replace(/\D/g, ''); // Remove tudo que não é dígito
                if (value.length > 9) {
                    value = value.replace(/^(\d{3})(\d{3})(\d{3})(\d{0,2}).*/, '$1.$2.$3-$4');
                } else if (value.length > 6) {
                    value = value.replace(/^(\d{3})(\d{3})(\d{0,3}).*/, '$1.$2.$3');
                } else if (value.length > 3) {
                    value = value.replace(/^(\d{3})(\d{0,3}).*/, '$1.$2');
                }
                e.target.value = value;
            });
        }

        // Máscara de CEP
        const cepInput = document.getElementById('cep');
        if (cepInput) {
            cepInput.addEventListener('input', (e) => {
                let value = e.target.value.replace(/\D/g, ''); // Remove tudo que não é dígito
                if (value.length > 5) {
                    value = value.replace(/^(\d{5})(\d{0,3}).*/, '$1-$2');
                }
                e.target.value = value;
            });
        }
    }

    /**
     * Configura a busca automática de endereço pelo CEP via API ViaCEP
     */
    function setupCEPLookup() {
        const cepInput = document.getElementById('cep');
        if (!cepInput) return;

        cepInput.addEventListener('blur', async () => {
            const cep = cepInput.value.replace(/\D/g, '');
            if (cep.length === 8) {
                try {
                    const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
                    const data = await response.json();
                    if (!data.erro) {
                        document.getElementById('endereco').value = data.logradouro;
                        document.getElementById('bairro').value = data.bairro;
                        document.getElementById('cidade').value = data.localidade;
                        document.getElementById('estado').value = data.uf;
                    } else {
                        alert('CEP não encontrado.');
                    }
                } catch (error) {
                    console.error('Erro ao buscar CEP:', error);
                    alert('Erro ao buscar CEP. Tente novamente.');
                }
            }
        });
    }
})();
