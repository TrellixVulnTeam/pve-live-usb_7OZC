��    K      t  e   �      `  $   a  &   �  )   �      �  #   �  -     *   J  +   u  =   �  )   �  ;   	  <   E      �  :   �     �     �      	     0	  $   L	     q	     �	  (   �	     �	     �	     
      
     :
     N
  '   g
  &   �
  "   �
  $   �
     �
  $        B      ]  #   ~  )   �  ,   �  0   �  "   *     M  /   g     �      �  !   �      �  #        >     Q  ?   i  4   �  -   �  4     4   A  $   v  &   �  ,   �     �  "        *  ;   C  *        �     �  %   �       �       �  �   �  5   t     �     �     �  �  �  #   �  (   �  6   �  $         B  2   c  /   �  0   �  6   �  /   .  5   ^  8   �  *   �  8   �     1     N  #   g     �  $   �      �     �          *     C  (   Z     �     �     �  5   �  +   �      +  %   L      r  %   �     �  %   �  !   �  .     1   M  5     '   �  (   �  A     $   H  (   m  .   �  (   �  $   �          .  F   F  :   �  -   �  6   �  9   -   0   g   -   �   7   �   "   �   +   !!  !   M!  B   o!  (   �!     �!     �!  &   "  "   7"  	  Z"    d&  �   ~'  6   )(     `(  &   �(     �(            	   <           =   K          -   )                  J                E   5   3      #   6      $   @   (   4      A   2           "           B   ;          *            &   
   I   F           1   !   ?       0      :             H   G       +                  9   ,           >   C                       '   7                      D       %   8   /      .       %s: %s doesn't exist, skipping call
 %s: %s is encrypted on real device %s
 %s: CD-ROM auto-eject command failed: %s
 %s: CD-ROM eject command failed
 %s: CD-ROM eject command succeeded
 %s: CD-ROM load from slot command failed: %s
 %s: CD-ROM select disc command failed: %s
 %s: CD-ROM select speed command failed: %s
 %s: CD-ROM select speed command not supported by this kernel
 %s: CD-ROM tray close command failed: %s
 %s: CD-ROM tray close command not supported by this kernel
 %s: CD-ROM tray toggle command not supported by this kernel
 %s: FindDevice called too often
 %s: IDE/ATAPI CD-ROM changer not supported by this kernel
 %s: SCSI eject failed
 %s: SCSI eject succeeded
 %s: `%s' can be mounted at `%s'
 %s: `%s' is a link to `%s'
 %s: `%s' is a multipartition device
 %s: `%s' is mounted at `%s'
 %s: `%s' is not a mount point
 %s: `%s' is not a multipartition device
 %s: `%s' is not mounted
 %s: closing tray
 %s: could not allocate memory
 %s: default device: `%s'
 %s: device is `%s'
 %s: device name is `%s'
 %s: disabling auto-eject mode for `%s'
 %s: enabling auto-eject mode for `%s'
 %s: error while allocating string
 %s: error while finding CD-ROM name
 %s: error while reading speed
 %s: exiting due to -n/--noop option
 %s: expanded name is `%s'
 %s: floppy eject command failed
 %s: floppy eject command succeeded
 %s: invalid argument to --auto/-a option
 %s: invalid argument to --cdspeed/-x option
 %s: invalid argument to --changerslot/-c option
 %s: invalid argument to -i option
 %s: listing CD-ROM speed
 %s: maximum symbolic link depth exceeded: `%s'
 %s: selecting CD-ROM disc #%d
 %s: setting CD-ROM speed to %dX
 %s: setting CD-ROM speed to auto
 %s: tape offline command failed
 %s: tape offline command succeeded
 %s: toggling tray
 %s: too many arguments
 %s: tried to use `%s' as device name but it is no block device
 %s: trying to eject `%s' using CD-ROM eject command
 %s: trying to eject `%s' using SCSI commands
 %s: trying to eject `%s' using floppy eject command
 %s: trying to eject `%s' using tape offline command
 %s: unable to eject, last error: %s
 %s: unable to exec umount of `%s': %s
 %s: unable to find or open device for: `%s'
 %s: unable to fork: %s
 %s: unable to open /etc/fstab: %s
 %s: unable to open `%s'
 %s: unable to read the speed from /proc/sys/dev/cdrom/info
 %s: unmount of `%s' did not exit normally
 %s: unmount of `%s' failed
 %s: unmounting `%s'
 %s: unmounting device `%s' from `%s'
 %s: using default device `%s'
 Eject version %s by Jeff Tranter (tranter@pobox.com)
Usage:
  eject -h				-- display command usage and exit
  eject -V				-- display program version and exit
  eject [-vnrsfqpm] [<name>]		-- eject device
  eject [-vn] -d			-- display default device
  eject [-vn] -a on|off|1|0 [<name>]	-- turn auto-eject feature on or off
  eject [-vn] -c <slot> [<name>]	-- switch discs on a CD-ROM changer
  eject [-vn] -t [<name>]		-- close tray
  eject [-vn] -T [<name>]		-- toggle tray
  eject [-vn] -i on|off|1|0 [<name>]	-- toggle manual eject protection on/off
  eject [-vn] -x <speed> [<name>]	-- set CD-ROM max speed
  eject [-vn] -X [<name>]		-- list CD-ROM available speeds
Options:
  -v	-- enable verbose output
  -n	-- don't eject, just show device found
  -r	-- eject CD-ROM
  -s	-- eject SCSI device
  -f	-- eject floppy
  -q	-- eject tape
  -p	-- use /proc/mounts instead of /etc/mtab
  -m	-- do not unmount device even if it is mounted
 Long options:
  -h --help   -v --verbose      -d --default
  -a --auto   -c --changerslot  -t --trayclose  -x --cdspeed
  -r --cdrom  -s --scsi         -f --floppy     -X --listspeed     -q --tape
  -n --noop   -V --version
  -p --proc   -m --no-unmount   -T --traytoggle
 Parameter <name> can be a device file or a mount point.
If omitted, name defaults to `%s'.
By default tries -r, -s, -f, and -q in order until success.
 eject version %s by Jeff Tranter (tranter@pobox.com)
 unable to open %s: %s
 usage: volname [<device-file>]
 volname Project-Id-Version: eject
Report-Msgid-Bugs-To: FULL NAME <EMAIL@ADDRESS>
POT-Creation-Date: 2008-11-04 23:19+0100
PO-Revision-Date: 2010-09-28 17:47+0000
Last-Translator: Andrej Znidarsic <andrej.znidarsic@gmail.com>
Language-Team: Slovenian <sl@li.org>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Launchpad-Export-Date: 2010-11-16 07:24+0000
X-Generator: Launchpad (build Unknown)
 %s: %s ne obstaja, klic preskočen
 %s: %s je šifriran na pravi napravi %s
 %s: ukaz samodejnega izmeta CD-ROM-a je spodletel: %s
 %s: ukaz izvrzi CD-ROM je spodletel
 %s: ukaz izvrzi CD-ROM je uspel
 %s: ukaz naloži iz reže CD-ROM je spodletel: %s
 %s: ukaz izbora medija CD-ROM je spodletel: %s
 %s: ukaz izberi hitrost CD-ROM je spodletel: %s
 %s: ukaz izberi hitrost CD-ROM ni podprt v temu jedru
 %s: ukaz zapri pladenj CD-ROM je spodletel: %s
 %s: ukaz zapri pladenj CD-ROM ni podprt v temu jedru
 %s: ukaz preklopi pladenj CD-ROM ni podprt v temu jedru
 %s: FindDevice je bil prepogosto poklican
 %s: IDE/ATAPI menjalec CD-ROM-ov ni podprt v temu jedru
 %s: izmet SCSI je spodletel
 %s: SCSI izmet je uspel
 %s: `%s' se lahko priklopi na `%s'
 %s: `%s' je povezava do `%s'
 %s: naprava `%s' ima več razdelkov
 %s: `%s' je priklopljen na `%s'
 %s: `%s' ni priklopna točka
 %s: `%s' ima le en razdelek
 %s: `%s' ni priklopljen
 %s: zapiranje pladnja
 %s: ni bilo mogoče dodeliti pomnilnika
 %s: privzeta naprava: `%s
 %s: naprava je`%s
 %s: ime naprave je `%s
 %s: onemogočanje načina samodejnega izmeta za `%s'
 %s: omogočanje samodejnega izmeta za `%s'
 %s: napaka med dodelitvijo niza
 %s: napaka med iskanjem imena CD-ROM
 %s: napaka med branjem hitrosti
 %s: izhod zaradi možnosti -n/--noop
 %s: razširjeno ime je `%s'
 %s: ukaz izvrzi disketo je spodletel
 %s: ukaz izvrzi disketo je uspel
 %s: neveljaven argument za možnost --auto/-a
 %s: neveljaven argument za možnost --cdspeed/-x
 %s: neveljaven argument za možnost --changerslot/-c
 %s: neveljaven argument za možnost -i
 %s: izpisovanje seznama hitrosti CD-ROM
 %s: najvišja globina simbolnih povezav je bila presežena: `%s'
 %s: izbiranje medija CD-ROM št. %d
 %s: nastavljanje hitrosti CD-ROM na %dX
 %s: nastavljanje hitrosti CD-ROM na samodejno
 %s: ukaz nepovezana kaseta je spodletel
 %s: ukaz nepovezana kaseta je uspel
 %s: preklapljanje pladnja
 %s: preveč argumentov
 %s: poskus uporabe `%s' kot imena naprave, vendar ni blokovna naprava
 %s: poskušanje izmeta `%s' z uporabo ukaza izvrzi CD-ROM
 %s: poskus izmeta `%s' z uporabo ukazov SCSI
 %s: poskus izmeta `%s' z uporabo ukaza izvrzi disketo
 %s: poskus izmeta `%s' z uporabo ukaza nepovezana kaseta
 %s: ni bilo mogoče izvreči, zadnja napaka: %s
 %s: odklopa `%s' ni bilo mogoče izvesti: %s
 %s: ni bilo mogoče najti ali odpreti naprave za: `%s'
 %s: ni bilo mogoče razvejiti: %s
 %s: ni bilo mogoče odpreti /etc/fstab: %s
 %s: `%s' ni bilo mogoče odpreti
 %s: hitrosti iz /proc/sys/dev/cdrom/info ni bilo mogoče prebrati
 %s: odklop `%s' se ni končal običajno
 %s: odklop `%s' je spodletel
 %s: odklapljanje `%s'
 %s: odklapljanje naprave `%s' iz `%s'
 %s: uporaba privzete naprave `%s'
 Različica Eject %s, Jeff Tranter (tranter@pobox.com)
Uporaba:
  eject -h				-- prikaže uporabo ukazov in konča
  eject -V				-- prikaže različico programa in konča
  eject [-vnrsfqpm] [<name>]		-- izvrže napravo
  eject [-vn] -d			-- prikaže privzeto napravo
  eject [-vn] -a on|off|1|0 [<name>]	-- vklopi/izklopi samodejni izmet
  eject [-vn] -c <slot> [<name>]	-- preklopi med mediji v menjalcu CD-ROM
  eject [-vn] -t [<name>]		-- zapri pladenj
  eject [-vn] -T [<name>]		-- preklopi pladenj
  eject [-vn] -i on|off|1|0 [<name>]	-- vklopi/izklopi zaščito pred ročnim izmetom
  eject [-vn] -x <speed> [<name>]	-- nastavi najvišjo hitrost CD-ROM max speed
  eject [-vn] -X [<name>]		-- Prikaži seznam razpoložljivih hitrosti CD-ROM
Možnosti:
  -v	-- omogoči podrobni izpis
  -n	-- ne izvrzi, samo prikaži najdeno napravo
  -r	-- izvrzi CD-ROM
  -s	-- izvrzi napravo SCSI
  -f	-- izvrzi disketo
  -q	-- izvrzi kaseto
  -p	-- uporabi /proc/mounts namesto /etc/mtab
  -m	-- ne odklopi naprave, četudi je priklopljena
 Razširjene možnosti:
  -h --help   -v --verbose      -d --default
  -a --auto   -c --changerslot  -t --trayclose  -x --cdspeed
  -r --cdrom  -s --scsi         -f --floppy     -X --listspeed     -q --tape
  -n --noop   -V --version
  -p --proc   -m --no-unmount   -T --traytoggle
 Parameter <name> je lahko datoteka naprave ali priklopna točka.
Če je izpuščen, se uporabi `%s'.
Privzeto poskuša -r, -s, -f, in -q,  v tem vrstnem redu, do uspeha.
 različica eject %s, Jeff Tranter (tranter@pobox.com)
 %s ni bilo mogoče odpreti: %s
 uporaba: volname [<datoteka naprave>]
 volname 