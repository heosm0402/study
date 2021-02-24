class Gun():
    def __init__(self, kind):
        self.kind = kind


    def bang(self):
        print('bang!!!')


class Police:
    def __init__(self):
        self.gun = None


    def acquire_gun(self, gun):
        self.gun = gun

    
    def release_gun(self):
        gun = self.gun
        self.gun = None
        return gun


    def shoot(self):
        if self.gun:
            self.gun.bang()
        else:
            print("No gun")


if __name__ == '__main__':
    p1 = Police()
    print("p1 shoots")
    p1.shoot()
    print()

    revolver = Gun('Revolver')
    p1.acquire_gun(revolver)
    revolver = None

    print('p1 shoots again')
    p1.shoot()
    print()

    revolver = p1.release_gun()
    print('p1 shoots again again')
    p1.shoot()
