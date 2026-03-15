# Voxel Camera System

## Português

### Sobre o projeto

O **Voxel Camera System** é um sistema **open source** criado inteiramente por mim.

Este projeto cria uma comunicação entre **Roblox** e **Minecraft** utilizando **requisições HTTP** para transmitir imagens de câmera entre os dois ambientes.

O sistema passou por diversas modificações e melhorias ao longo do desenvolvimento até chegar à versão atual.

Tecnologias utilizadas no projeto:

- Python
- Luau (Roblox)
- HTML

---

## Tutorial

Se você chegou até aqui, provavelmente quer aprender como utilizar o sistema.

---

## Roblox

Depois que o seu site estiver **publicamente acessível**, altere a URL usada no Roblox para:

```
{seulink}/cameraGet
```

Existem dois modos disponíveis:

`/videos`  
Utiliza vídeos enviados para o repositório do GitHub.

`/`  
Utiliza a câmera e salva as imagens localmente no sistema.

---

## Minecraft

No Minecraft o sistema funciona de forma diferente.

Ele utiliza **um plugin de servidor**, não um mod.

O plugin adiciona **dois comandos principais**.

### Comandos

`/telao`

Este comando fornece ao jogador **um mapa que reproduz o conteúdo vindo do endpoint `/cameraGet`**.

`/telao2`

Este comando cria **uma tela flutuante feita com partículas**, que também reproduz o conteúdo vindo do sistema.

Para remover a tela flutuante de partículas, basta executar o comando:

```
/telao2 reset
```

---

## Configuração do Minecraft

1. Inicie o servidor normalmente.
2. Depois desligue o servidor.
3. Vá até a pasta:

```
/plugins
```

4. Procure a pasta:

```
VoxelScreen
```

5. Dentro dela você encontrará arquivos `.yml`.

Abra o arquivo:

```
config.yml
```

Neste arquivo existe um campo onde você deve inserir a **URL do seu sistema**.

Exemplo:

```
https://seusite.com
```

É obrigatório incluir `https://`, caso contrário o sistema não funcionará.

Também existem configurações relacionadas à tela de partículas (`telao2`), como:

- Espaçamento entre partículas
- Tamanho da tela

Observação:  
A configuração de tamanho **não funciona na versão 1.12.2**, que é a versão principal suportada pelo plugin.

---

# English

## About the Project

The **Voxel Camera System** is an **open-source project** created entirely by **tavoxx**.

This project creates communication between **Roblox** and **Minecraft** using **HTTP requests** to transmit camera images between the two environments.

The system went through multiple modifications and improvements during development until reaching its current state.

Technologies used in this project:

- Python
- Luau (Roblox)
- HTML

---

## Tutorial

If you are here, you probably want to learn how to use the system.

---

## Roblox

Once your website is **publicly accessible**, change the Roblox URL to:

```
{yourlink}/cameraGet
```

Two modes are available:

`/videos`  
Uses videos uploaded to the GitHub repository.

`/`  
Uses the camera and stores images locally in the system.

---

## Minecraft

In Minecraft the system works differently.

It uses **a server plugin**, not a mod.

The plugin adds **two main commands**.

### Commands

`/telao`

This command gives the player **a map that reproduces the content from the `/cameraGet` endpoint**.

`/telao2`

This command creates **a floating screen made of particles** that displays the same camera output.

To remove the floating particle screen, simply run the command:

```
/telao2 reset
```

---

## Minecraft Configuration

1. Start the server normally.
2. Then stop the server.
3. Go to the folder:

```
/plugins
```

4. Look for the folder:

```
VoxelScreen
```

5. Inside it you will find `.yml` files.

Open the file:

```
config.yml
```

Inside this file you will find a field where you must insert **your system URL**.

Example:

```
https://yourwebsite.com
```

You must include `https://`, otherwise the system will not work.

There are also configuration options related to the particle screen (`telao2`), such as:

- Particle spacing
- Screen size

Note:  
The size configuration **does not work in version 1.12.2**, which is the main supported version of the plugin.
