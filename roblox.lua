--[[ TavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavox
TavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavoxTavox
TavoxTavoxTavoxTavoxTavoxTavoxTavoxTavox]]--



local HttpService = game:GetService("HttpService")

local PART_NAME = "ScreenPart"
local URL = "{yourlink}/cameraGet"

local SIZE = 64
local PIXEL_SIZE = 3

local part = workspace:WaitForChild(PART_NAME)

local gui = Instance.new("SurfaceGui")
gui.Parent = part
gui.Face = Enum.NormalId.Front
gui.CanvasSize = Vector2.new(SIZE * PIXEL_SIZE, SIZE * PIXEL_SIZE)

local container = Instance.new("Frame")
container.Parent = gui
container.Size = UDim2.fromScale(1,1)
container.BackgroundTransparency = 1

local pixels = {}

for y = 0, SIZE - 1 do
    for x = 0, SIZE - 1 do
        local p = Instance.new("Frame")
        p.Parent = container
        p.Size = UDim2.fromOffset(PIXEL_SIZE, PIXEL_SIZE)
        p.Position = UDim2.fromOffset(
        x * PIXEL_SIZE,
        y * PIXEL_SIZE
        )
        p.BorderSizePixel = 0
        p.BackgroundColor3 = Color3.new(0,0,0)
        
        pixels[y * SIZE + x + 1] = p
    end
end

while true do
    local success, response = pcall(function()
        return HttpService:GetAsync(URL)
    end)
    
    if success then
        local data = HttpService:JSONDecode(response)
        
        if data.ready and data.data then
            for i, rgb in ipairs(data.data) do
                pixels[i].BackgroundColor3 =
                Color3.fromRGB(rgb[1], rgb[2], rgb[3])
            end
        end
    end
    
    task.wait(0.05)
end

