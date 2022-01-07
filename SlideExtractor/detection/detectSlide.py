from .difference import difference


def detectSlide(frame,prevSlide,method="difference"):
    if method=="difference":
        changed=difference(frame,prevSlide)
        return(changed)
