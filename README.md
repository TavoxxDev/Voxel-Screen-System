<p align="center">
  <h1 align="center">Voxel Camera System</h1>
  <p align="center">
    A bridge between Roblox and Minecraft using HTTP camera streaming
  </p>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-Backend-blue)
![Roblox](https://img.shields.io/badge/Roblox-Luau-red)
![Minecraft](https://img.shields.io/badge/Minecraft-Plugin-green)
![License](https://img.shields.io/badge/License-Open%20Source-lightgrey)

</p>

---

# About

The **Voxel Camera System** is an **open source project** created entirely by **tavoxx**.

The goal of this project is to create a communication bridge between **Roblox** and **Minecraft**, allowing camera frames to be transmitted using **HTTP requests**.

The system has gone through multiple improvements and modifications during development until reaching its current version.

### Technologies

| Technology | Usage |
|-----------|------|
| Python | Backend server |
| Luau | Roblox communication |
| HTML | Camera interface |
| Minecraft Plugin | Rendering screens |

---

# Tutorial

If you are here, you probably want to learn how to use the system.

---

# Roblox Setup

Once your website is **publicly available**, change the Roblox URL to:

```
{yourlink}/cameraGet
```

Available modes:

| Mode | Description |
|-----|-------------|
| `/videos` | Uses videos uploaded to GitHub |
| `/` | Uses the camera and stores images locally |

---

# Minecraft

In Minecraft the system works using a **server plugin**, not a mod.

The plugin adds commands that allow players to view the camera output inside the game.

---

# Commands

| Command | Description |
|--------|-------------|
| `/telao` | Gives the player a map displaying the camera stream |
| `/telao2` | Creates a floating particle screen displaying the camera |
| `/telao2 reset` | Removes the floating particle screen |

### Portuguese

| Comando | Descrição |
|--------|-------------|
| `/telao` | Dá ao jogador um mapa exibindo a câmera |
| `/telao2` | Cria uma tela flutuante feita de partículas |
| `/telao2 reset` | Remove a tela flutuante de partículas |

---

# Minecraft Configuration

1. Start the server normally
2. Stop the server
3. Go to the folder:

```
/plugins
```

4. Open the folder:

```
VoxelScreen
```

5. Open the file:

```
config.yml
```

Inside this file you must insert your system URL.

Example:

```
https://yourwebsite.com
```

**Important**

You must include `https://` in the URL, otherwise the system will not work.

---

### Particle Screen Settings

The plugin also includes configuration options for the particle screen (`/telao2`):

- Particle spacing
- Screen size

Note:

The screen size configuration **does not work in version 1.12.2**, which is the main supported version of the plugin.

---

# License

This project is open source and available for modification and distribution.
