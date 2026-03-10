# Voxel Camera System

## 🇧🇷 Português

### Sobre o projeto
O **Voxel Camera System** é um sistema **open source** criado inteiramente por **tavoxx**.

Talvez você esteja se perguntando: **“O que esse sistema faz?”**

Ele cria uma comunicação entre **Roblox** e **Minecraft** utilizando um sistema de **requisições HTTP** para transmitir imagens ou videos da câmera.  
(O sistema não utiliza WebSockets.)

Durante o desenvolvimento, o sistema passou por várias modificações e melhorias até chegar à versão atual.

O projeto utiliza as seguintes tecnologias:

- Python
- Luau (Roblox)
- HTML

---

### Tutorial

Se você chegou até aqui, provavelmente quer aprender a usar o sistema.

---

### Roblox

Depois que o seu site estiver **publicamente acessível**, altere a URL usada no Roblox para:

```
URL: {seulink}/cameraGet
```

Você pode usar dois modos:

- `/videos` → usa vídeos enviados para o GitHub
- `/` → usa a câmera e salva as fotos localmente no sistema

---

### Minecraft

No Minecraft o sistema funciona de forma diferente.

Ele utiliza **um plugin de servidor**, não um mod.

Existem **dois comandos disponíveis**:

#### `/telao`

Executar esse comando irá fornecer ao jogador **um mapa que reproduz o conteúdo vindo de `/cameraGet`**.

#### `/telao2`

Esse comando funciona de forma semelhante ao primeiro, porém:

- Em vez de um mapa
- Ele cria **uma tela feita com partículas** que reproduz o conteúdo da câmera.

---

### Configuração do Minecraft

1. Inicie o servidor normalmente.
2. Depois **desligue o servidor**.
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

Nesse arquivo você encontrará um campo onde deve inserir a **URL do seu sistema**.

⚠️ Sempre inclua:

```
https://
```

Caso contrário, o sistema **não funcionará**.

Também existem configurações para o sistema de partículas (`telao2`), como:

- Espaçamento das partículas
- Tamanho da tela

⚠️ O ajuste de tamanho **não funciona na versão 1.12.2**, que é a versão principal suportada pelo plugin.

---

# 🇺🇸 English

## About the Project

The **Voxel Camera System** is an **open-source project** created entirely by **tavoxx**.

You might be wondering: **“What does this system do?”**

It creates communication between **Roblox** and **Minecraft** using **HTTP requests** to transmit camera images.  
(The system does not use WebSockets.)

During development, the system went through multiple modifications and improvements until reaching its current state.

The project uses the following technologies:

- Python
- Luau (Roblox)
- HTML

---

## Tutorial

If you're here, you probably want to learn how to use the system.

---

## Roblox

Once your website is **publicly available**, change the Roblox URL to:

```
URL: {yourlink}/cameraGet
```

You can use two modes:

- `/videos` → uses videos uploaded to GitHub
- `/` → uses the camera and stores images locally

---

## Minecraft

In Minecraft the system works differently.

It uses a **server plugin**, not a mod.

There are **two available commands**:

### `/telao`

This command gives the player **a map that reproduces what is happening in `/cameraGet`**.

### `/telao2`

This command works similarly to the first one, but instead:

- Instead of giving a map
- It creates **a particle screen** that displays the camera output.

---

## Minecraft Configuration

1. Start your server normally.
2. Then **stop the server**.
3. Go to the folder:

```
/plugins
```

4. Look for the folder:

```
VoxelScreen
```

5. Inside it you will find `.yml` files.

Open:

```
config.yml
```

In this file you will find a field where you must insert your **system URL**.

⚠️ Always include:

```
https://
```

Otherwise the system **will not work**.

There are also configuration settings for the particle screen (`telao2`), such as:

- Particle spacing
- Screen size

⚠️ The size configuration **does not work in version 1.12.2**, which is the main supported version of the plugin.
