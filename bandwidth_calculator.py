#bpp is equal 1
print("Input bpp value")
bpp = int(input())
print("Input height value")
h = int(input())
print("Input width value")
w = int(input())
print("Input hz value")
hz = int(input())
bwc = (bpp * h * w * hz)
bwc_mbps = (bwc / 1024 / 1024)
print(f'bwc = {bwc} bps.')
print(f'bwc = {bwc_mbps} mbps.')
