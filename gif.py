import imageio
imagename= ['img1.JPG', 'img2.JPG']
image=[] # to store image

for i in imagename:
    image.append(imageio.imread(i))
imageio.mimsave('shadi.gif', image, duration=0.5)

