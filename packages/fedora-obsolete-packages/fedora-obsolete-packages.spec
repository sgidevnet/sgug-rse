# Provenpackagers are welcome to modify this package, but please don't obsolete
# additional packages without a corresponding bugzilla ticket being filed.

# Please remember to add all of the necessary information.  See below the
# Source0: line for a description of the format.  It is important that
# everything be included; yanking packages from an end-user system is "serious
# business" and should not be done lightly or without making everything as
# clear as possible.

# Finally, please keep python2 obsoletes together, since there is bound to be a
# significant number of them.

Name:       fedora-obsolete-packages
# Please keep the version equal to the targeted Fedora release
Version:    31
Release:    43
Summary:    A package to obsolete retired packages

# This package has no actual content; there is nothing to license.
License:    Public Domain
URL:        https://docs.fedoraproject.org/en-US/packaging-guidelines/#renaming-or-replacing-existing-packages
BuildArch:  noarch

Source0:    README

# ===============================================================================
# Skip down below these convenience macros
%define obsolete_ticket() %{lua:
    local ticket = rpm.expand('%1')

    -- May need to declare the master structure
    if type(obs) == 'nil' then
        obs = {}
    end

    if ticket == '%1' then
        rpm.expand('%{error:No ticket provided to obsolete_ticket}')
    end

    if ticket == 'Ishouldfileaticket' then
        ticket = nil
    end

    -- Declare a new set of obsoletes
    local index = #obs+1
    obs[index] = {}
    obs[index].ticket = ticket
    obs[index].list = {}
}

%define obsolete() %{lua:
    local pkg = rpm.expand('%1')
    local ver = rpm.expand('%2')

    if pkg == '%1' then
        rpm.expand('%{error:No package name provided to obsolete}')
    end
    if ver == '%2' then
        rpm.expand('%{error:No version provided to obsolete}')
    end

    if not string.find(ver, '-') then
        rpm.expand('%{error:You must provide a version-release, not just a version.}')
    end

    local o = pkg .. ' < ' .. ver
    print('Obsoletes: ' .. o)

    -- Append this obsolete to the last set of obsoletes in the list
    local list = obs[#obs].list
    list[#list+1] = o
}

# Don't use this macro!  Only here because people keep doing this wrong.
%define obsolete_wrong() %{lua:
    local pkg = rpm.expand('%1')
    local ver = rpm.expand('%2')

    if pkg == '%1' then
        rpm.expand('%{error:No package name provided to obsolete}')
    end
    if ver == '%2' then
        rpm.expand('%{error:No version provided to obsolete}')
    end

    local o = pkg .. ' < ' .. ver
    print('Obsoletes: ' .. o)

    -- Append this obsolete to the last set of obsoletes in the list
    local list = obs[#obs].list
    list[#list+1] = o
}


%define list_obsoletes %{lua:
    local i
    local j
    for i = 1,#obs do
        if obs[i].ticket ~= nil and string.find(obs[i].ticket, '1578359') then
            print('Plus the following python2 packages, in accordance with the general switch away\\n')
            print('from Python2 ahead of its retirement in 2020.  See\\n')
            print('https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3 for more\\n')
            print('information.\\n\\n')
        end

        for j = 1,#obs[i].list do
            print('  ' .. obs[i].list[j] .. '\\n')
        end
        if obs[i].ticket == nil then
            print('  (No ticket was provided!)\\n\\n')
        else
            print('  (See ' .. obs[i].ticket .. ')\\n\\n')
        end
    end
}

# ===============================================================================
# Add calls to the obsolete_ticket and obsolete macros below, along with a note
# indicating the Fedora version in which the entries can be removed.  This is
# generally three releases beyond whatever release Rawhide is currently.  The
# macros make this easy, and will automatically update the package description.

# The ticket information is important.  Please don't add things here without
# having a filed ticket, preferrably in bugzilla.

# All Obsoletes: entries MUST be versioned (including the release), with the
# version being the same as or just higher than the last version-release of the
# obsoleted package.  This allows the package to return to the distribution
# later.  The best possible thing to do is to find the last version-release
# which was in the distribution, add one to the release, and add that version
# without using a dist tag.  This allows a rebuild with a bumped Release: to be
# installed.

# And don't forget to update the package description!


# Template:
# Remove in F33
# %%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1234567
# %%obsolete foo 3.5-7

# ========================================
# Please place non-python2 Obsoletes: here
# ========================================

# Remove in F33: retired in F30
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1747428
%obsolete gegl 0.2.0-41

# Remove in F33: retired in F31
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1702954
%obsolete california 0.4.0-19

# Remove in F33: retired in F30+
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1700073
%obsolete mongodb 4.0.3-4
%obsolete mongodb-server 4.0.3-4
%obsolete mongodb-test 4.0.3-4

# Remove in F33; retired in F30+
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1696965
%obsolete appcenter 3.1.1-2
%obsolete appcenter-gnome-shell-search-provider 3.1.1-2

# Remove in F33
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1680068
%obsolete empathy 3.12.14-9

# Remove in F33
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1707567
%obsolete yumex 3.0.17-3

# Remove in F33
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1707570
%obsolete pix 1.8.2-2

# Remove in F33
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1707577
%obsolete system-config-services 0.111.4-4

# Remove in F32 - FTBFS since F26
%obsolete_ticket https://pagure.io/fesco/issue/2080
%obsolete trafficserver 5.3.0-14
%obsolete trafficserver-devel 5.3.0-14
%obsolete trafficserver-perl 5.3.0-14

# Remove in F32
# Someone added this without supplying a ticket, and didn't include a release,
# either.
%obsolete_ticket Ishouldfileaticket
%obsolete_wrong gedit-plugin-dashboard 3.31.4

# Remove in F32
# Someone added this without supplying a ticket!
%obsolete_ticket Ishouldfileaticket
%obsolete wxBase 2.8.12-32
%obsolete wxGTK 2.8.12-32
%obsolete wxGTK-devel 2.8.12-32
%obsolete wxGTK-gl 2.8.12-32
%obsolete wxGTK-media 2.8.12-32

# Remove in F32
# Someone added this without supplying a ticket!
%obsolete_ticket Ishouldfileaticket
%obsolete vala-compat 0.18.1-13
%obsolete vala-compat-devel 0.18.1-13
%obsolete vala-compat-doc 0.18.1-13
%obsolete vala-compat-tools 0.18.1-13

# Remove in F32
# https://lists.fedoraproject.org/archives/list/python-devel@lists.fedoraproject.org/message/VTOQDUSGTMGOZOJHK4Y6GNVVLHA36QEC/
%obsolete_ticket https://src.fedoraproject.org/rpms/fedora-obsolete-packages/pull-request/16
%obsolete python33 3.3.7-7

# Remove in F32
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1696209
%obsolete python2-PyXB 1.2.6-5
%obsolete python2-PyXB-doc 1.2.6-5
%obsolete python3-PyXB 1.2.6-5
%obsolete python3-PyXB-doc 1.2.6-5

# Remove in F33: retired in F30
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1644813
%obsolete fedmsg-notify 0.5.9-10

# Remove in F33: retired in F31
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1747430
%obsolete gcompris 15.11-1
%obsolete gcompris-administration 15.11-1
%obsolete gcompris-sound-af 15.11-1
%obsolete gcompris-sound-ar 15.11-1
%obsolete gcompris-sound-ast 15.11-1
%obsolete gcompris-sound-bg 15.11-1
%obsolete gcompris-sound-br 15.11-1
%obsolete gcompris-sound-ca 15.11-1
%obsolete gcompris-sound-cs 15.11-1
%obsolete gcompris-sound-da 15.11-1
%obsolete gcompris-sound-de 15.11-1
%obsolete gcompris-sound-el 15.11-1
%obsolete gcompris-sound-en 15.11-1
%obsolete gcompris-sound-eo 15.11-1
%obsolete gcompris-sound-es 15.11-1
%obsolete gcompris-sound-eu 15.11-1
%obsolete gcompris-sound-fi 15.11-1
%obsolete gcompris-sound-fr 15.11-1
%obsolete gcompris-sound-gd 15.11-1
%obsolete gcompris-sound-he 15.11-1
%obsolete gcompris-sound-hi 15.11-1
%obsolete gcompris-sound-hu 15.11-1
%obsolete gcompris-sound-id 15.11-1
%obsolete gcompris-sound-it 15.11-1
%obsolete gcompris-sound-kn 15.11-1
%obsolete gcompris-sound-lt 15.11-1
%obsolete gcompris-sound-mr 15.11-1
%obsolete gcompris-sound-nb 15.11-1
%obsolete gcompris-sound-nl 15.11-1
%obsolete gcompris-sound-nn 15.11-1
%obsolete gcompris-sound-pa 15.11-1
%obsolete gcompris-sound-pt 15.11-1
%obsolete gcompris-sound-ru 15.11-1
%obsolete gcompris-sound-sk 15.11-1
%obsolete gcompris-sound-sl 15.11-1
%obsolete gcompris-sound-so 15.11-1
%obsolete gcompris-sound-sr 15.11-1
%obsolete gcompris-sound-sv 15.11-1
%obsolete gcompris-sound-th 15.11-1
%obsolete gcompris-sound-tr 15.11-1
%obsolete gcompris-sound-ur 15.11-1
%obsolete gcompris-sound-zh_CN 15.11-1

# Remove in F34
%obsolete_ticket https://src.fedoraproject.org/rpms/aeskulap/c/eb0558f61370d8b08285159f887abea4a80334ed
%obsolete aeskulap 0.2.2-0.38

# ==========================================
# Please collect the python2 Obsoletes: here
# ==========================================

# Remove in F32
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1578359
%obsolete ambari 1.5.1-12
%obsolete ambari-agent 1.5.1-12
%obsolete ambari-client 1.5.1-12
%obsolete ambari-server 1.5.1-12
%obsolete aubio-python2 0.4.6-3
%obsolete contextkit 0.5.41-20
%obsolete cryptlib-python2 3.4.4-12
%obsolete fts-rest 3.8.3-2
%obsolete fts-rest-cloud-storage 3.8.3-2
%obsolete fts-rest-http-authz-signed-cert 3.8.3-2
%obsolete fts-rest-oauth2 3.8.3-2
%obsolete gmpy 1.17-14
%obsolete lekhonee 0.7-18
%obsolete link-grammar-python2 5.5.1-5
%obsolete mesos 0.23.0-1
%obsolete mesos-devel 0.23.0-1
%obsolete mesos-java 0.23.0-1
%obsolete pulp-admin-client 2.15.2-3
%obsolete pulp-agent 2.15.2-3
%obsolete pulp-consumer-client 2.15.2-3
%obsolete pulp-docker-admin-extensions 3.1.1-2
%obsolete pulp-docker-plugins 3.1.1-2
%obsolete pulp-nodes-admin-extensions 2.15.2-3
%obsolete pulp-nodes-child 2.15.2-3
%obsolete pulp-nodes-common 2.15.2-3
%obsolete pulp-nodes-consumer-extensions 2.15.2-3
%obsolete pulp-nodes-parent 2.15.2-3
%obsolete pulp-ostree-admin-extensions 1.3.0-3
%obsolete pulp-ostree-plugins 1.3.0-3
%obsolete pulp-puppet-admin-extensions 2.15.2-3
%obsolete pulp-puppet-consumer-extensions 2.15.2-3
%obsolete pulp-puppet-devel 2.15.2-3
%obsolete pulp-puppet-handlers 2.15.2-3
%obsolete pulp-puppet-plugins 2.15.2-3
%obsolete pulp-puppet-tools 2.15.2-3
%obsolete pulp-python-admin-extensions 2.0.2-2
%obsolete pulp-python-plugins 2.0.2-2
%obsolete pulp-rpm-admin-extensions 2.15.2-3
%obsolete pulp-rpm-consumer-extensions 2.15.2-3
%obsolete pulp-rpm-devel 2.15.2-3
%obsolete pulp-rpm-handlers 2.15.2-3
%obsolete pulp-rpm-plugins 2.15.2-3
%obsolete pulp-server 2.15.2-3
%obsolete pycryptopp 0.7-1
%obsolete pygoocanvas 0.14.1-25
%obsolete pygtkchart 0-0.16
%obsolete pylibpcap 0.6.4-18
%obsolete pyode 1.2.0-24
%obsolete pypar-mpich 2.1.5_108-23
%obsolete pypar-openmpi 2.1.5_108-23
%obsolete PyQuante 1.6.5-14
%obsolete PyQuante-libint 1.6.5-14
%obsolete PySBIG 0.04-23
%obsolete python-ceph-compat 2:14.2.0-1
%obsolete python-cephfs 2:14.2.0-1
%obsolete python-libasyncns 0.7.1-21
%obsolete python-libpamtest 1.0.7-2
%obsolete python-mesos 0.23.0-1
%obsolete python-oslo-context-tests 2.20.0-2
%obsolete python-oslo-middleware 3.34.0-2
%obsolete python-oslo-middleware-tests 3.34.0-2
%obsolete python-pyblock 0.53-18
%obsolete python-pylons 1.0.1-4
%obsolete python-rados 2:14.2.0-1
%obsolete python-rbd 2:14.2.0-1
%obsolete python-rgw 2:14.2.0-1
%obsolete python-xpyb-devel 1.3.1-12
%obsolete python2-abrt 2.10.11-1
%obsolete python2-abrt-addon 2.10.11-1
%obsolete python2-abrt-container-addon 2.10.11-1
%obsolete python2-adns 1.2.1-24
%obsolete python2-afl 0.7-5
%obsolete python2-alsa 1.1.6-5
%obsolete python2-alsaaudio 0.8.2-10
%obsolete python2-assimp 3.3.1-17
%obsolete python2-assimulo 2.9-29
%obsolete python2-astropy 3.0.5-2
%obsolete python2-astroscrappy 1.0.5-13
%obsolete python2-backports-lzma 0.0.2-20
%obsolete python2-basemap 1.0.7-30
%obsolete python2-beecrypt 4.2.1-22
%obsolete python2-behave 1.2.6-1
%obsolete python2-blockdev 2.20-3
%obsolete python2-blockdiag-devel 1.5.4-2
%obsolete python2-bloom 0.7.2-4
%obsolete python2-blosc 1.5.1-3
%obsolete python2-bodhi 3.12.0-101
%obsolete python2-bodhi-client 3.12.0-101
%obsolete python2-botan 1.10.17-11
%obsolete python2-boto3 1.7.41-2
%obsolete python2-brial 1.2.4-2
%obsolete python2-caribou 0.4.21-13
%obsolete python2-cartopy 0.16.0-7
%obsolete python2-catkin_tools 0.4.4-8
%obsolete python2-cccolutils 1.5-12
%obsolete python2-cdb 0.34-21
%obsolete python2-certbot 0.31.0-3
%obsolete python2-chemps2 1.8.9-2
%obsolete python2-cinderclient 3.5.0-2
%obsolete python2-clearsilver 0.10.5-52
%obsolete python2-collectd_systemd 0.0.1-0.11
%obsolete python2-compreffor 0.4.6-7
%obsolete python2-cotyledon 1.6.7-9
%obsolete python2-cotyledon-tests 1.6.7-9
%obsolete python2-couchbase 2.5.0-2
%obsolete python2-cradox 2.1.0-4
%obsolete python2-createrepo_c 0.11.1-3
%obsolete python2-cryptominisat 5.6.5-2
%obsolete python2-csvkit 1.0.3-4
%obsolete python2-ctags 1.0.5-22
%obsolete python2-cups 1.9.74-3
%obsolete python2-cvxopt 1.2.2-2
%obsolete python2-cypari2 1.3.1-2
%obsolete python2-cypari2-devel 1.3.1-2
%obsolete python2-cysignals 1.7.2-2
%obsolete python2-cysignals-devel 1.7.2-2
%obsolete python2-daap 0.7.1-25
%obsolete python2-designateclient 2.9.0-3
%obsolete python2-designateclient-tests 2.9.0-3
%obsolete python2-dlib 19.4-11
%obsolete python2-dnf 5.0-1
%obsolete python2-dnf-plugin-kickstart 5.0-1
%obsolete python2-dnf-plugin-leaves 5.0-1
%obsolete python2-dnf-plugin-local 5.0-1
%obsolete python2-dnf-plugin-migrate 5.0-1
%obsolete python2-dnf-plugin-show-leaves 5.0-1
%obsolete python2-dnf-plugin-snapper 5.0-1
%obsolete python2-dnf-plugin-system-upgrade 5.0-1
%obsolete python2-dnf-plugin-tracer 5.0-1
%obsolete python2-dnf-plugin-versionlock 5.0-1
%obsolete python2-dnf-plugins-core 5.0-1
%obsolete python2-dnf-plugins-extras-common 5.0-1
%obsolete python2-dnfdaemon 0.3.19-5
%obsolete python2-eccodes 2.8.2-4
%obsolete python2-ecryptfs-utils 111-15
%obsolete python2-editdist 0.3-21
%obsolete python2-elemental-mpich 0.87.5-3
%obsolete python2-elemental-openmpi 0.87.5-3
%obsolete python2-envisage 4.6.0-2
%obsolete python2-espresso-mpich 4.0.0-1
%obsolete python2-espresso-openmpi 4.0.0-1
%obsolete python2-fedbadges 0.5.2-11
%obsolete python2-fedora-turbogears 0.10.0-8
%obsolete python2-fedora-turbogears2 0.10.0-8
%obsolete python2-fiona 1.8-0.3
%obsolete python2-flake8 3.7.7-2
%obsolete python2-flann 1.8.4-19
%obsolete python2-forensic1394 0.2-23
%obsolete python2-fpylll 0.4.1dev-3
%obsolete python2-gd 0.56-21
%obsolete python2-gdal 2.3.2-8
%obsolete python2-gdcm 2.8.4-12
%obsolete python2-gdl 0.9.8-7
%obsolete python2-genders 1.22-19
%obsolete python2-gensim-addons 0.10.0-17
%obsolete python2-gensim-test 0.10.0-17
%obsolete python2-geos 3.6.1-11
%obsolete python2-getdata 0.10.0-10
%obsolete python2-gexiv2 0.10.10-2
%obsolete python2-giacpy 0.6.6-5
%obsolete python2-giacpy-devel 0.6.6-5
%obsolete python2-glanceclient 1:2.10.0-2
%obsolete python2-gmpy2 2.1.0-0.6
%obsolete python2-gpod 0.8.3-26
%obsolete python2-gpsd 3.18.1-2
%obsolete python2-gr-iio 0.2-6
%obsolete python2-grib_api 1.27.0-3
%obsolete python2-gstreamer-rtsp 0.10.8-20
%obsolete python2-guppy 0.1.10-12
%obsolete python2-h5py 2.9.0-4
%obsolete python2-hamlib 3.3-4
%obsolete python2-hawkey 0.31.0-13
%obsolete python2-healpy 1.12.4-3
%obsolete python2-hidapi 0.7.99.post20-11
%obsolete python2-hivex 1.3.15-12
%obsolete python2-hokuyoaist 3.0.2-25
%obsolete python2-imdb 5.1-10
%obsolete python2-imgcreate 1:25.0-12
%obsolete python2-ipaclient 4.8-1
%obsolete python2-ipalib 4.8-1
%obsolete python2-ipdb 0.11-10
%obsolete python2-ipykernel 5.1.0-20
%obsolete python2-ipython 5.8.0-20
%obsolete python2-ipython-sphinx 5.8.0-20
%obsolete python2-ipython-tests 5.8.0-20
%obsolete python2-iscsi-initiator-utils 6.2.0.876-6
%obsolete python2-isort 4.3.4-7
%obsolete python2-isprelink 0.1.2-27
%obsolete python2-josepy 1.1.0-7
%obsolete python2-jpype 0.6.3-9
%obsolete python2-jsmva 6.14.06-2
%obsolete python2-jupyroot 6.14.06-2
%obsolete python2-jupyter-client 5.2.3-10
%obsolete python2-jupyter-core 4.4.0-9
%obsolete python2-keycloak-httpd-client-install 0.8-9
%obsolete python2-keystoneclient 1:3.15.0-2
%obsolete python2-keystoneclient-tests 1:3.15.0-2
%obsolete python2-kmod 0.9-23
%obsolete python2-kolab 1.0.2-10
%obsolete python2-kolabformat 1.1.6-7
%obsolete python2-lcms2 0.1-9
%obsolete python2-ldns 1.7.0-23
%obsolete python2-ledger 3.1.1-21
%obsolete python2-lhapdf 6.2.1-5
%obsolete python2-libarchive 3.1.2.1-17
%obsolete python2-libarchive-c 2.8-4
%obsolete python2-libcap-ng 0.7.9-6
%obsolete python2-libcomps 0.2-1
%obsolete python2-libconcord 1.3-4
%obsolete python2-libdiscid 0.4.1-18
%obsolete python2-libdnet 1.12-29
%obsolete python2-libdnf 0.31.0-13
%obsolete python2-libfreenect 0.5.7-5
%obsolete python2-libftdi 1.3-17
%obsolete python2-libhid 0.2.17-35
%obsolete python2-libieee1284 0.2.11-29
%obsolete python2-libipa_hbac 3.0-1
%obsolete python2-libkml 1.3.0-17
%obsolete python2-liblinear 1.94-18
%obsolete python2-libnl3 3.4.0-7
%obsolete python2-libnuml 1.1.1-11
%obsolete python2-libpoly 0.1.7-2
%obsolete python2-libproxy 0.4.15-11
%obsolete python2-librepo 2.0-1
%obsolete python2-libreport 2.9.6-1
%obsolete python2-libsbml 5.17.0-8
%obsolete python2-libsedml 1:0.4.3-16
%obsolete python2-libssh2 0.7.1-22
%obsolete python2-libsss_nss_idmap 2.1.0-20
%obsolete python2-libsvm 3.23-4
%obsolete python2-libteam 1.27-12
%obsolete python2-libwfut 0.2.3-18
%obsolete python2-libxc 4.2.3-2
%obsolete python2-lilv 0.24.4-4
%obsolete python2-line_profiler 2.1-4
%obsolete python2-llfuse 1.3.5-3
%obsolete python2-lmdb 0.92-8
%obsolete python2-louis 3.7.0-3
%obsolete python2-lupa 1.6-6
%obsolete python2-lxc 0.1-4
%obsolete python2-lzo 1.09-14
%obsolete python2-macaroons 0.3.0-3
%obsolete python2-mapnik 0.1-42
%obsolete python2-mathgl 2.4.1-11
%obsolete python2-mayavi 4.6.2-2
%obsolete python2-MDAnalysis 0.18.0-3
%obsolete python2-med 3.3.1-5
%obsolete python2-metakernel 0.20.14-10
%obsolete python2-metakernel-bash 0.20.14-10
%obsolete python2-metakernel-echo 0.20.14-10
%obsolete python2-metakernel-python 0.20.14-10
%obsolete python2-metakernel-tests 0.20.14-10
%obsolete python2-ming 0.4.8-13
%obsolete python2-mlt 6.12.0-2
%obsolete python2-ModulemdTranslationHelpers 0.5-4
%obsolete python2-moose 3.1.4-2
%obsolete python2-muranoclient 1.0.1-2
%obsolete python2-music21 2.2.1-14
%obsolete python2-mwlib 0.15.19-5
%obsolete python2-nbconvert 5.3.1-11
%obsolete python2-nbformat 4.4.0-7
%obsolete python2-nest 2.16.0-4
%obsolete python2-nest-mpich 2.16.0-4
%obsolete python2-nest-openmpi 2.16.0-4
%obsolete python2-netcdf4 1.3.1-2
%obsolete python2-networkx-drawing 2.2-3
%obsolete python2-networkx-geo 2.2-3
%obsolete python2-neutronclient 6.7.0-3
%obsolete python2-nlopt 2.4.2-19
%obsolete python2-notebook 5.7.8-2
%obsolete python2-novaclient 1:10.1.0-4
%obsolete python2-odcs-client 0.2.23-4
%obsolete python2-odcs-common 0.2.23-4
%obsolete python2-omniORB 4.2.2-11
%obsolete python2-openbabel 2.4.1-17
%obsolete python2-opencv 3.4.1-7
%obsolete python2-openfst 1.6.9-2
%obsolete python2-openimageio 1.8.14-3
%obsolete python2-openmeeg 2.4-0.5
%obsolete python2-openms 2.3.0-14.fc30
%obsolete python2-openslide 1.1.1-12
%obsolete python2-openstack-doc-tools 1.8.0-7
%obsolete python2-openstackclient 3.14.1-5
%obsolete python2-openstackdocstheme 1.29.0-4
%obsolete python2-openstacksdk-tests 0.12.0-6
%obsolete python2-osc-lib 1.9.0-5
%obsolete python2-osc-lib-tests 1.9.0-5
%obsolete python2-oslo-cache 1.28.0-2
%obsolete python2-oslo-concurrency 3.25.1-2
%obsolete python2-oslo-concurrency-tests 3.25.1-2
%obsolete python2-oslo-config 2:5.2.0-4
%obsolete python2-oslo-context 2.20.0-2
%obsolete python2-oslo-db 4.33.1-8
%obsolete python2-oslo-db-tests 4.33.1-8
%obsolete python2-oslo-i18n 3.19.0-3
%obsolete python2-oslo-log 3.36.0-2
%obsolete python2-oslo-log-tests 3.36.0-2
%obsolete python2-oslo-messaging 5.35.1-2
%obsolete python2-oslo-messaging-tests 5.35.1-2
%obsolete python2-oslo-policy 1.33.2-3
%obsolete python2-oslo-privsep 1.13.0-9
%obsolete python2-oslo-serialization 2.24.0-2
%obsolete python2-oslo-service 1.29.0-2
%obsolete python2-oslo-service-tests 1.29.0-2
%obsolete python2-oslo-utils 3.35.1-4
%obsolete python2-oslo-utils-tests 3.35.1-4
%obsolete python2-oslo-versionedobjects 1.31.3-3
%obsolete python2-oslo-vmware 2.26.0-3
%obsolete python2-osmium 2.14.3-3
%obsolete python2-owfs 3.2p2-5
%obsolete python2-owslib 0.17.0-4
%obsolete python2-pcp 4.1.3-2
%obsolete python2-pep8-naming 0.4.1-12
%obsolete python2-petsc4py-mpich 3.9.1-4
%obsolete python2-petsc4py-openmpi 3.9.1-4
%obsolete python2-pivy 0.5.0-22
%obsolete python2-pjsua 2.7.2-4
%obsolete python2-player 3.1.0-13
%obsolete python2-plyvel 1.0.4-6
%obsolete python2-pocketsphinx 5prealpha-3
%obsolete python2-poppler-qt4 0.18.1-18
%obsolete python2-portmidi 217-27
%obsolete python2-posix_ipc 0.9.8-20
%obsolete python2-prelude 4.1.0-9
%obsolete python2-preludedb 4.1.0-6
%obsolete python2-protocols 1.0-0.32
%obsolete python2-psi 0.3-0.21
%obsolete python2-pulp-agent-lib 2.15.2-3
%obsolete python2-pulp-bindings 2.15.2-3
%obsolete python2-pulp-client-lib 2.15.2-3
%obsolete python2-pulp-common 2.15.2-3
%obsolete python2-pulp-devel 2.15.2-3
%obsolete python2-pulp-docker-common 3.1.1-2
%obsolete python2-pulp-oid_validation 2.15.2-3
%obsolete python2-pulp-ostree-common 1.3.0-3
%obsolete python2-pulp-puppet-common 2.15.2-3
%obsolete python2-pulp-python-common 2.0.2-2
%obsolete python2-pulp-repoauth 2.15.2-3
%obsolete python2-pulp-rpm-common 2.15.2-3
%obsolete python2-pulp-streamer 2.15.2-3
%obsolete python2-py-bcrypt 0.4-20
%obsolete python2-py4j 0.10.7-4
%obsolete python2-pybind11 2.2.3-5
%obsolete python2-pybloomfiltermmap 0.3.15-12
%obsolete python2-pycadf 2.4.0-8
%obsolete python2-pyclipper 1.1.0-4
%obsolete python2-pycosat 0.6.3-6
%obsolete python2-pycryptodomex 3.6.6-3
%obsolete python2-pyeclib 1.5.0-9
%obsolete python2-pyev 0.9.0-0.5
%obsolete python2-pyfits 3.5-7
%obsolete python2-pygit2 0.27.2-3
%obsolete python2-pygraphviz 1.3-4
%obsolete python2-pygrib 2.0.3-2
%obsolete python2-pygsl 2.3.0-4
%obsolete python2-pygsl-devel 2.3.0-4
%obsolete python2-pyhunspell 0.5.4-7
%obsolete python2-pyicu 2.0.3-3
%obsolete python2-pyliblo 0.10.0-12
%obsolete python2-pylibmc 1.5.1-12
%obsolete python2-pylint 1.9.0-3
%obsolete python2-pymilia 1.0.0-25
%obsolete python2-pymongo 3.7.1-3
%obsolete python2-pymongo-gridfs 3.7.1-3
%obsolete python2-pymssql 2.1.3-7
%obsolete python2-pymtp 0.0.6-15
%obsolete python2-PyMuPDF 1.13.20-3
%obsolete python2-pyodbc 3.0.10-15
%obsolete python2-pyopengl-tk 3.1.1a1-14
%obsolete python2-pyproj 1.9.6-3
%obsolete python2-pyqtgraph 0.10.0-6
%obsolete python2-pytaglib 1.4.3-5
%obsolete python2-pytest-flake8 1.0.1-4
%obsolete python2-pythia8 8.2.35-6
%obsolete python2-pyudev 0.21.0-10
%obsolete python2-pyudev-glib 0.21.0-10
%obsolete python2-pyudev-pyside 0.21.0-10
%obsolete python2-pyudev-qt4 0.21.0-10
%obsolete python2-pyudev-qt5 0.21.0-10
%obsolete python2-pyudev-wx 0.21.0-10
%obsolete python2-pyuv 1.4.0-14
%obsolete python2-pyx 0.14.1-11
%obsolete python2-qgis 2.18.20-2
%obsolete python2-qhexedit2 0.8.4-2
%obsolete python2-qhexedit2-qt5 0.8.4-2
%obsolete python2-qrcode 5.1-15
%obsolete python2-qrcode-core 5.1-15
%obsolete python2-qrencode 1.2~git.1.b75219e-2
%obsolete python2-QtAwesome 0.4.4-8
%obsolete python2-qtconsole 4.3.1-7
%obsolete python2-rackspace-auth-openstack 1.3-13
%obsolete python2-rasterio 1.0.2-4
%obsolete python2-rdkit 2018.03.4-3
%obsolete python2-rdopkg 0.49.0-2
%obsolete python2-re2 1.0.5-10
%obsolete python2-redland 1.0.16.1-29
%obsolete python2-releases 1.6.0-3
%obsolete python2-remctl 3.14-3
%obsolete python2-resultsdb_conventions-fedora 2.0.3-8
%obsolete python2-rhn-check 2.9.12-3
%obsolete python2-rhn-client-tools 2.9.12-3
%obsolete python2-rhn-setup 2.9.12-3
%obsolete python2-rhn-setup-gnome 2.9.12-3
%obsolete python2-rpkg 1.57-7
%obsolete python2-rtslib 2.1.fb69-4
%obsolete python2-ryu 4.29-3
%obsolete python2-saga 2.2.7-10
%obsolete python2-samba 2:4.10.0-1
%obsolete python2-samba-dc 2:4.10.0-1
%obsolete python2-samba-test 2:4.10.0-1
%obsolete python2-satyr 0.27-1
%obsolete python2-scikit-image 0.14.0-6
%obsolete python2-scikit-learn 0.19.1-7
%obsolete python2-scrypt 0.8.0-8
%obsolete python2-scss 1.3.5-5
%obsolete python2-shapely 1.6.4-3
%obsolete python2-shogun 6.0.0-16
%obsolete python2-shout 0.2.1-23
%obsolete python2-slip 0.6.4-14
%obsolete python2-slip-dbus 0.6.4-14
%obsolete python2-slip-gtk 0.6.4-14
%obsolete python2-smartcols 0.3.0-6
%obsolete python2-smbc 1.0.15.4-19
%obsolete python2-smbpasswd 1.0.1-40
%obsolete python2-snack 2.2.11-1
%obsolete python2-SoapySDR 0.6.1-3
%obsolete python2-solv 0.7.4-12
%obsolete python2-sphinxbase 5prealpha-5
%obsolete python2-sphinxcontrib-phpdomain 0.4.1-5
%obsolete python2-ssh2-python 0.15.0-4
%obsolete python2-sss 2.1.0-20
%obsolete python2-sss-murmur 2.1.0-20
%obsolete python2-stestr-sql 2.1.0-3
%obsolete python2-stfl 0.22-29
%obsolete python2-stp 2.3.1-5
%obsolete python2-subscription-manager-rhsm 1.24.2-2
%obsolete python2-subunit2sql 1.9.0-2
%obsolete python2-sword 1.8.1-10
%obsolete python2-tbb 2019.1-2
%obsolete python2-testify 0.11.0-13
%obsolete python2-tg-devtools 2.3.11-5
%obsolete python2-tgcaptcha2 0.3.1-10
%obsolete python2-tlsh 3.4.5-10
%obsolete python2-tracer 0.7.1-3
%obsolete python2-trademgen 1.00.2-20
%obsolete python2-traitlets 4.3.2-10
%obsolete python2-tre 0.8.0-26
%obsolete python2-uinput 0.10.1-21
%obsolete python2-urjtag 2018.06-4
%obsolete python2-uwsgidecorators 2.0.18-9
%obsolete python2-v8 6.7.17-9
%obsolete python2-vigra 1.11.1-11
%obsolete python2-vips 8.6.5-5
%obsolete python2-virtkey 0.63.0-11
%obsolete python2-virtualenvwrapper 4.8.2-9
%obsolete python2-vitrageclient 2.1.0-2
%obsolete python2-volume_key 0.3.12-2
%obsolete python2-vrpn 7.33-15
%obsolete python2-vtk 8.1.1-4
%obsolete python2-vtk-mpich 8.1.1-4
%obsolete python2-vtk-mpich-qt 8.1.1-4
%obsolete python2-vtk-openmpi 8.1.1-4
%obsolete python2-vtk-openmpi-qt 8.1.1-4
%obsolete python2-vtk-qt 8.1.1-4
%obsolete python2-webm 0.2.2-20
%obsolete python2-xapps-overrides 1.4.0-2
%obsolete python2-xklavier 0.2-24
%obsolete python2-xmlsec 1.3.3-5
%obsolete python2-xpyb 1.3.1-12
%obsolete python2-xrootd 4.8.5-3
%obsolete python2-XStatic-Angular 1:1.5.8.0-7
%obsolete python2-XStatic-Angular-Bootstrap 2.2.0.0-7
%obsolete python2-XStatic-Angular-Gettext 2.1.0.2-12
%obsolete python2-XStatic-Angular-lrdragndrop 1.0.2.2-13
%obsolete python2-XStatic-Angular-Mock 1.2.1.1-14
%obsolete python2-XStatic-Angular-UUID 0.0.4.0-6
%obsolete python2-XStatic-Angular-Vis 4.16.0.0-3
%obsolete python2-XStatic-Bootstrap-Datepicker 1.3.1.0-13
%obsolete python2-XStatic-Bootstrap-SCSS 3.3.7.1-7
%obsolete python2-XStatic-bootswatch 3.3.7.0-8
%obsolete python2-XStatic-D3 3.5.17.0-7
%obsolete python2-XStatic-DataTables 1.10.15.1-8
%obsolete python2-XStatic-FileSaver 1.3.2.0-3
%obsolete python2-XStatic-Font-Awesome 4.7.0.0-7
%obsolete python2-XStatic-Hogan 2.0.0.2-14
%obsolete python2-XStatic-Jasmine 2.4.1.1-6
%obsolete python2-XStatic-JQuery-Migrate 1.2.1.1-14
%obsolete python2-XStatic-JQuery-quicksearch 2.0.3.1-14
%obsolete python2-XStatic-JQuery-TableSorter 2.14.5.1-14
%obsolete python2-XStatic-jquery-ui 1.12.0.1-6
%obsolete python2-XStatic-JS-Yaml 3.8.1.0-4
%obsolete python2-XStatic-JSEncrypt 2.3.1.1-6
%obsolete python2-XStatic-Json2yaml 0.1.1.0-3
%obsolete python2-XStatic-Magic-Search 0.2.5.1-9
%obsolete python2-XStatic-mdi 1.4.57.0-10
%obsolete python2-XStatic-Patternfly 3.21.0.1-8
%obsolete python2-XStatic-Patternfly-Bootstrap-Treeview 2.1.3.2-8
%obsolete python2-XStatic-QUnit 1.14.0.2-14
%obsolete python2-XStatic-Rickshaw 1.5.0.0-16
%obsolete python2-XStatic-roboto-fontface 0.5.0.0-10
%obsolete python2-XStatic-smart-table 1.4.13.2-6
%obsolete python2-XStatic-Spin 1.2.5.2-15
%obsolete python2-XStatic-termjs 0.0.7.0-6
%obsolete python2-yara 3.8.1-4
%obsolete python2-yenc 0.4.0-16
%obsolete python2-yui 1.1.2-13
%obsolete python2-z3 4.8.1-2
%obsolete python2-zinnia 0.06-42
%obsolete python2-zookeeper 3.4.9-13
%obsolete pyxmlsec 0.3.1-13
%obsolete RunSnakeRun 2.0.4-11
%obsolete statscache-common 0.0.4-10
%obsolete statscache-consumer 0.0.4-10
%obsolete statscache-web 0.0.4-10
%obsolete system-config-date 1.10.9-4
%obsolete TurboGears 1.1.3-21
%obsolete zbar-pygtk 0.20.1-4

# Remove in F33
%obsolete autocloud-backend 0.8.0-6
%obsolete autocloud-common 0.8.0-6
%obsolete autocloud-web 0.8.0-6
%obsolete bkchem 0.14.0-21
%obsolete bmpanel2-cfg 2.1-0.24
%obsolete bpython 0.18-2
%obsolete broctl 2.5.4-5
%obsolete bugyou_plugins 0.1.6-6
%obsolete cas 1.0-15
%obsolete catkin 0.4.5-20
%obsolete childsplay 1.6-30
%obsolete cwiid-python2 0.6.00-30
%obsolete darkserver 2.0-6
%obsolete darkserver-importer 2.0-6
%obsolete dreampie 1.1.1-18
%obsolete driconf 0.9.1-31
%obsolete emacs-pymacs 0.25-9
%obsolete fedocal 0.16-3
%obsolete fedora-motd 0.1.2-7
%obsolete firmware-tools 2.1.15-6
%obsolete flr 0.0.4-8
%obsolete fwbackups 1.43.7-7
%obsolete fwfstab 0.04-0.17
%obsolete galternatives 0.13.4-27
%obsolete genbackupdata 1.9-10
%obsolete github2fedmsg 0.3.6-10
%obsolete gitifyhg 0.8.4-13
%obsolete gnome-activity-journal 0.8.0-15
%obsolete gnue-common 0.6.9-17
%obsolete gofed-gofedlib 1.0.0-0.23
%obsolete gofed-infra 1.0.0-0.23
%obsolete gofed-resources  1.0.0-0.23
%obsolete googsystray 1.3.1-14
%obsolete gscribble 0.1.2-17
%obsolete gwsmhg 0.13.2-16
%obsolete hamster-time-tracker 2.0-0.17
%obsolete igor 0.4.1-12
%obsolete igor-client 0.4.1-12
%obsolete igor-common 0.4.1-12
%obsolete kimchi 1.5.1-12
%obsolete labyrinth 0.6-17
%obsolete loggerhead 1.18.2-10
%obsolete londonlaw 0.3.0-0.13
%obsolete loopabull 0.0.6-7
%obsolete mash 0.6.19-9
%obsolete memaker 20100110-20
%obsolete meta-test-family 0.8.0-5
%obsolete modularity-testing-framework 0.5.1-6
%obsolete mysql-utilities 1.5.6-8
%obsolete nagios-plugins-lfc 0.9.6-10
%obsolete nagstamon 1.0.1-8
%obsolete nautilus-pastebin 0.7.2-10
%obsolete nested 1.2.2-23
%obsolete ninja-ide 2.3-10
%obsolete nordugrid-arc-acix-cache 5.4.4-2
%obsolete nordugrid-arc-gangliarc 1.0.2-8
%obsolete nxt_python 2.2.2-7
%obsolete obmenu 1.0-29
%obsolete ocfs2console 1.8.5-11
%obsolete oggconvert 0.3.3-22
%obsolete openteacher 3.2-13
%obsolete pdc-updater 0.9.3-3
%obsolete pkpgcounter 3.50-18
%obsolete pmpu 0.2-20
%obsolete pondus 0.8.0-15
%obsolete pycam 0.5.1-12
%obsolete pyfribidi 0.11.0-19
%obsolete pygtkglext 1.1.0-31
%obsolete pygtksourceview 2.10.1-19
%obsolete pykde4 4.14.3-31
%obsolete pyliblzma 0.5.3-26
%obsolete PyPE 2.9.4-12
%obsolete PyQwt 5.2.0-43
%obsolete pyroom 0.4.1-20
%obsolete python-egenix-mx-base-devel 3.2.9-9
%obsolete python-gencpp-devel 0.3.4-15
%obsolete python-genpy-devel 0.3.7-17
%obsolete python-jabberbot 0.15-5
%obsolete python-reportlab-doc 3.4.0-11
%obsolete python2-ahkab 0.18-15
%obsolete python2-amara 1.2.0.2-25
%obsolete python2-amqp 2.4.1-2
%obsolete python2-anymarkup 0.5.0-13
%obsolete python2-anymarkup-core 0.5.0-14
%obsolete python2-anyvc 0.3.7.1-16
%obsolete python2-appindicator 12.10.0-26
%obsolete python2-apsw 3.24.0.r1-3
%obsolete python2-ase 3.16.2-6
%obsolete python2-autobahn 19.3.2-2
%obsolete python2-backports-unittest_mock 1.2.1-8
%obsolete python2-betamax 0.8.1-5
%obsolete python2-Bottleneck 1.2.1-9
%obsolete python2-breathe 4.7.3-7
%obsolete python2-broccoli 2.5.4-5
%obsolete python2-cairosvg 1.0.20-11
%obsolete python2-carddav 0.7.0-13
%obsolete python2-case 1.5.2-10
%obsolete python2-catkin-sphinx 0.3.1-2
%obsolete python2-celery 4.2.1-5
%obsolete python2-cliapp 1.20180121-2
%obsolete python2-cliff 2.13.0-3
%obsolete python2-cmdsignature 1.0.0-0.23
%obsolete python2-cmusphinx3 0.8-33
%obsolete python2-copr 1.90-2
%obsolete python2-coveralls 1.2.0-7
%obsolete python2-cracklib 2.9.6-20
%obsolete python2-curtsies 0.3.0-5
%obsolete python2-datanommer-models 0.9.1-7
%obsolete python2-dbusmock 0.18.3-3
%obsolete python2-deltarpm 3.6-30
%obsolete python2-deprecation 2.0.6-2
%obsolete python2-django1.11 1.11.20-2
%obsolete python2-django1.11-doc 1.11.20-2
%obsolete python2-docker 3.5.0-2
%obsolete python2-dropbox 9.4.0-2
%obsolete python2-egenix-mx-base 3.2.9-9
%obsolete python2-elfdata 0.6-11
%obsolete python2-epdb 0.15-10
%obsolete python2-fabric3 1.13.1-9
%obsolete python2-factory-boy 2.11.1-5
%obsolete python2-falcon 1.4.1-7
%obsolete python2-fedmsg 1.1.1-5
%obsolete python2-fedmsg-meta-debian 0.1-15
%obsolete python2-fedmsg-meta-fedora-infrastructure 0.27.0-3
%obsolete python2-flask-openid 1.2.5-14
%obsolete python2-flickrapi 2.2.1-6
%obsolete python2-fmn 2.1.1-4
%obsolete python2-fmn-lib 0.8.2-9
%obsolete python2-freeradius 3.0.21-3
%obsolete python2-future 0.18.2-4
%obsolete python2-gamin 0.1.10-34
%obsolete python2-gencpp 0.3.4-15
%obsolete python2-genlisp 0.3.3-15
%obsolete python2-genpy 0.3.7-17
%obsolete python2-gerrit-view 0.3.2-12
%obsolete python2-gerritlib 0.6.0-9
%obsolete python2-gertty 1.5.0-6
%obsolete python2-gitdb 2.0.3-6
%obsolete python2-GitPython 2.1.11-3
%obsolete python2-google-api-client 1:1.6.7-7
%obsolete python2-gpaw 1.4.0-11
%obsolete python2-gpg 1.13.1-8
%obsolete python2-grokmirror 1.1.1-2
%obsolete python2-hacking 1.1.0-6
%obsolete python2-hardware 0.18-13
%obsolete python2-hardware-detect 0.18-13
%obsolete python2-intervaltree 2.1.0-5
%obsolete python2-ioprocess 1.1.0-4
%obsolete python2-jedi 0.12.1-4
%obsolete python2-jenkins 0.4.15-7
%obsolete python2-jenkins-job-builder 1:2.1.0-3
%obsolete python2-jsonpath-rw 1.2.3-19
%obsolete python2-jsonpath-rw-ext 1.2.0-2
%obsolete python2-jsonschema 2.6.0-10
%obsolete python2-keystoneauth1 3.4.0-4
%obsolete python2-kickstart 3.20-3
%obsolete python2-koji 1.20.0-2
%obsolete python2-koji-cli-plugins 1.20.0-2
%obsolete python2-koji-containerbuild-cli 0.7.13.1-2
%obsolete python2-kombu 1:4.2.2-3
%obsolete python2-langtable 0.0.43-4
%obsolete python2-larch 1.20151025-10
%obsolete python2-lazr-smtptest 2.0.3-10
%obsolete python2-libemu 0.2.0-11
%obsolete python2-libfdt 1.4.7-4
%obsolete python2-libguestfs 1:1.40.2-5
%obsolete python2-libiptcdata 1.0.4-21
%obsolete python2-libmodulemd 2.9.3-2
%obsolete python2-libmodulemd1 1.8.16-2
%obsolete python2-librtfcomp 1.1-27
%obsolete python2-libselinux 2.9-5
%obsolete python2-libsemanage 2.9-3
%obsolete python2-libturpial 1.7.0-12
%obsolete python2-libvirt 5.1.0-3
%obsolete python2-lldb 8.0.0-2
%obsolete python2-lunatic 1.0.1-0.26
%obsolete python2-lz4 2.1.2-3
%obsolete python2-mandrill 1.0.51-14
%obsolete python2-markdown 2.6.11-6
%obsolete python2-matplotlib-gtk 2.2.5-2
%obsolete python2-matplotlib-gtk3 2.2.5-2
%obsolete python2-matplotlib-qt4 2.2.5-2
%obsolete python2-matplotlib-qt5 2.2.5-2
%obsolete python2-migrate 0.12.0-4
%obsolete python2-moksha-hub 1.5.17-2
%obsolete python2-moksha-wsgi 1.2.4-12
%obsolete python2-morbid 0.8.7.3-20
%obsolete python2-mox3 0.17.0-9
%obsolete python2-mpi4py-mpich 3.0.1-2
%obsolete python2-mpi4py-openmpi 3.0.1-2
%obsolete python2-multilib 1.2-8
%obsolete python2-ndg_httpsclient 0.4.0-14
%obsolete python2-neo4j-driver 1.6.2-3
%obsolete python2-neomodel 3.3.1-2
%obsolete python2-nose-cover3 0.1.0-24
%obsolete python2-nose-progressive 1.5.1-16
%obsolete python2-nose-xcover 1.0.11-3
%obsolete python2-nototools 0-0.20190710
%obsolete python2-nss 1.0.1-15
%obsolete python2-numexpr 2.6.6-3
%obsolete python2-numpydoc 0.8.0-6
%obsolete python2-opensips 2.4.7-2
%obsolete python2-openstacksdk 0.12.0-4
%obsolete python2-os-client-config 1.28.0-7
%obsolete python2-pandas 0.23.4-3
%obsolete python2-pandas-datareader 0.6.0-7
%obsolete python2-paste-script 2.0.2-9
%obsolete python2-pep8 1.7.1-4
%obsolete python2-pkgwat 0.11-13
%obsolete python2-pmw 2.0.0-13
%obsolete python2-policycoreutils 2.9-5
%obsolete python2-postman 0.6.0-17
%obsolete python2-praw 3.6.2-3
%obsolete python2-psphere 0.5.2-16
%obsolete python2-pudb 2017.1.4-5
%obsolete python2-pungi 4.1.38-2
%obsolete python2-pwntools 3.12.2-2
%obsolete python2-pwquality 1.4.0-13
%obsolete python2-pyaff 3.7.18-3
%obsolete python2-pyaudio 0.2.11-3
%obsolete python2-PyDrive 1.3.1-8
%obsolete python2-pyfakefs 3.1-7
%obsolete python2-pykafka 2.6.0-0.6
%obsolete python2-pylibravatar 1.6-20
%obsolete python2-pypam 0.5.0-41
%obsolete python2-pypump 0.6-14
%obsolete python2-pytest-cache 1.0-17
%obsolete python2-pytest-catchlog 1.2.2-12
%obsolete python2-pytest-forked 1.0.2-3
%obsolete python2-pytest-pep8 1.0.6-18
%obsolete python2-pytest-shutil 1.2.6-7
%obsolete python2-pytest-timeout 1.3.3-5
%obsolete python2-pytest-tornado 0.8.0-2
%obsolete python2-pytest-vcr 1.0.1-2
%obsolete python2-pytest-virtualenv 1.2.11-11
%obsolete python2-pytest-watch 4.1.0-12
%obsolete python2-pytest-xdist 1.29.0-3
%obsolete python2-qt5-webengine 5.12.1-6
%obsolete python2-rapi 0.15.2-17
%obsolete python2-raven 6.9.0-5
%obsolete python2-requests-toolbelt 0.9.1-2
%obsolete python2-requests_ntlm 1.1.0-5
%obsolete python2-rhev 1.0-16
%obsolete python2-robosignatory 0.5.0-5
%obsolete python2-root 6.18.00-4
%obsolete python2-rootplot 2.2.2-9
%obsolete python2-rosinstall 0.7.8-5
%obsolete python2-routes 2.4.1-9
%obsolete python2-rpyc 4.0.1-4
%obsolete python2-rra 0.14-20
%obsolete python2-sanlock 3.6.0-9
%obsolete python2-scipy-doc 1.2.0-2
%obsolete python2-setools 4.1.1-15
%obsolete python2-simplemediawiki 1.2.0-0.18
%obsolete python2-snappy 0.5.3-3
%obsolete python2-snowballstemmer 1.2.1-11
%obsolete python2-sphinx 1:2.0.0~b1-2
%obsolete python2-sphinx-intl 0.9.11-7
%obsolete python2-sphinx-notfound-page 0.4-3
%obsolete python2-sphinx-theme-alabaster 0.7.12-5
%obsolete python2-sphinx_rtd_theme 0.4.3-3
%obsolete python2-sphinxcontrib-httpdomain 1.7.0-5
%obsolete python2-sphinxcontrib-websupport 1.1.0-2
%obsolete python2-sphinxtrain 1.0.8-47
%obsolete python2-sqlalchemy-utils 0.32.12-10
%obsolete python2-squaremap 1.0.3-12
%obsolete python2-stevedore 1.28.0-3
%obsolete python2-stomper 0.4.1-11
%obsolete python2-stomppy 4.1.21-3
%obsolete python2-subvertpy 0.10.1-6
%obsolete python2-summershum 0.1.5-12
%obsolete python2-tables 3.4.4-5
%obsolete python2-tahrir 0.9.2-7
%obsolete python2-tahrir-api 0.8.1-10
%obsolete python2-terminado 0.8.1-7
%obsolete python2-tornado 5.0.2-6
%obsolete python2-totpcgi 0.5.5-19
%obsolete python2-trollius 2.1-11
%obsolete python2-tw2-core 2.2.3-14
%obsolete python2-tw2-dynforms 2.0.1-18
%obsolete python2-tw2-excanvas 2.0.2-16
%obsolete python2-tw2-forms 2.2.6-3
%obsolete python2-tw2-jit 2.0.3-19
%obsolete python2-tw2-jqplugins-flot 2.0.1-17
%obsolete python2-tw2-jqplugins-gritter 2.0.1-16
%obsolete python2-tw2-jqplugins-ui 2.3.0-7
%obsolete python2-tw2-jquery 2.2.0.2-9
%obsolete python2-tw2-sqla 2.0.6-15
%obsolete python2-txaio 18.8.1-2
%obsolete python2-txsocksx 1.15.0.2-11
%obsolete python2-unbound 1.8.3-8
%obsolete python2-urwidtrees 1.0-11
%obsolete python2-vatnumber 1.2-12
%obsolete python2-vdsm 4.18.999-448
%obsolete python2-virtualenv 16.0.0-8
%obsolete python2-virtualenv-api 2.1.16-7
%obsolete python2-virtualenv-clone 0.2.6-13
%obsolete python2-virtualenv-python26 16.0.0-8
%obsolete python2-warlock 1.3.0-9
%obsolete python2-watchdog 0.8.3-12
%obsolete python2-webhelpers 1.3-21
%obsolete python2-websocket-client 0.54.0-2
%obsolete python2-winrm 0.3.0-5
%obsolete python2-xmms2 0.8-59
%obsolete python2-yaql 1.1.3-7
%obsolete pyvnc2swf 0.9.5-26
%obsolete pywebkitgtk 1.1.8-14
%obsolete qct 1.7-21
%obsolete qct-mercurial 1.7-21
%obsolete rb_libtorrent-python2 1.1.13-3
%obsolete repo_manager 0.1.0-15
%obsolete revelation 0.4.14-21
%obsolete rssdler 0.4.2-18
%obsolete scout 0.4-24
%obsolete shinken 2.4.3-16
%obsolete sK1 0.9.1-0.20
%obsolete snake 0.11.1-13
%obsolete snap 0.6-14
%obsolete Spawning 0.9.7-8
%obsolete specto 0.4.1-16
%obsolete sphinx-webtools 0.2.1-20120541
%obsolete stonevpn 0.4.17-4
%obsolete stylus-toolbox 0.2.7-17
%obsolete supybot-fedmsg 0.2.0-9
%obsolete supybot-fedora 0.4.2-3
%obsolete supybot-koji 0.2-18
%obsolete supybot-meetbot 0.1.4-27
%obsolete synce-kpm 0.15.1-14
%obsolete synce-sync-engine 0.15.1-18
%obsolete syncthing-gtk 0.9.4.4-2
%obsolete system-config-users 1.3.8-7
%obsolete system-config-users-docs 1.0.9-16
%obsolete testoob 1.13-23
%obsolete the-new-hotness 0.10.0-6
%obsolete trac-sphinx-plugin 0.2.1-20120528
%obsolete translation-filter 1.0-16
%obsolete translation-filter-kde 1.0-16
%obsolete tunir 0.17.3-7
%obsolete turpial 3.0-13
%obsolete uwsgi-plugin-python2 2.0.18-9
%obsolete vdsm 4.18.999-448
%obsolete vdsm-api 4.18.999-448
%obsolete vdsm-hook-vmfex-dev 4.18.999-448
%obsolete vdsm-jsonrpc 4.18.999-448
%obsolete vdsm-xmlrpc 4.18.999-448
%obsolete vdsm-yajsonrpc 4.18.999-448
%obsolete viewvc 1.1.26-10
%obsolete virtaal 0.7.1-15
%obsolete wicd-common 1.7.4-10
%obsolete wordgroupz 0.3.1-18
%obsolete writetype 1.2.130-19
%obsolete wuja 0.0.8-22
%obsolete yum-axelget 1.0.5.1-11
%obsolete yum-langpacks 0.4.5-11
%obsolete yum-metadata-parser 1.1.4-23
%obsolete yum-utils 1.1.31-520

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1684162
%obsolete yum-NetworkManager-dispatcher 1.1.31-520
%obsolete yum-plugin-aliases 1.1.31-520
%obsolete yum-plugin-auto-update-debug-info 1.1.31-520
%obsolete yum-plugin-changelog 1.1.31-520
%obsolete yum-plugin-copr 1.1.31-520
%obsolete yum-plugin-fastestmirror 1.1.31-520
%obsolete yum-plugin-filter-data 1.1.31-520
%obsolete yum-plugin-fs-snapshot 1.1.31-520
%obsolete yum-plugin-keys 1.1.31-520
%obsolete yum-plugin-list-data 1.1.31-520
%obsolete yum-plugin-local 1.1.31-520
%obsolete yum-plugin-merge-conf 1.1.31-520
%obsolete yum-plugin-ovl 1.1.31-520
%obsolete yum-plugin-post-transaction-actions 1.1.31-520
%obsolete yum-plugin-priorities 1.1.31-520
%obsolete yum-plugin-protectbase 1.1.31-520
%obsolete yum-plugin-ps 1.1.31-520
%obsolete yum-plugin-puppetverify 1.1.31-520
%obsolete yum-plugin-refresh-updatesd 1.1.31-520
%obsolete yum-plugin-remove-with-leaves 1.1.31-520
%obsolete yum-plugin-rpm-warm-cache 1.1.31-520
%obsolete yum-plugin-show-leaves 1.1.31-520
%obsolete yum-plugin-tmprepo 1.1.31-520
%obsolete yum-plugin-tsflags 1.1.31-520
%obsolete yum-plugin-upgrade-helper 1.1.31-520
%obsolete yum-plugin-verify 1.1.31-520
%obsolete yum-plugin-versionlock 1.1.31-520
# we have python2-pyglet-1.3.2-3.fc29, but no python2-pyglet-1.3.2-3.fc30, use version from F31
%obsolete python-pyglet 1.4.1-1

# https://bugzilla.redhat.com/show_bug.cgi?id=1752361
%obsolete python2-pillow-tk 6.0.0-3
%obsolete python2-pillow-qt 6.0.0-3

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1750135
%obsolete python2-acme 0.31.0-2

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1751211
%obsolete python2-CommonMark 0.7.5-3

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1750138
%obsolete python2-parsedatetime 2.4-10

%obsolete_ticket https://src.fedoraproject.org/rpms/crypto-utils/c/1dab4d23a2a59b63abe52b9650ec8679e8faf301
%obsolete crypto-utils 2.5-5

%obsolete_ticket https://src.fedoraproject.org/rpms/PyQwt/c/33ed6350df04eea7f797b3e8d96995e9c63ea135
%obsolete PyQwt 5.2.0-60

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1675241
%obsolete kupfer 208-16

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1751418
%obsolete mingw64-webkitgtk 2.4.11-7
%obsolete mingw32-webkitgtk 2.4.11-7
%obsolete mingw64-webkitgtk3 2.4.11-7
%obsolete mingw32-webkitgtk3 2.4.11-7

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1751419
%obsolete packagedb-cli 2.14.1-10

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1751345
%obsolete nbdkit-python2-plugin 1.12.6-2

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1751591
%obsolete xfce4-hamster-plugin 1.7-23

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1751913
%obsolete mono-debugger 2.10-22

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1752016
%obsolete fedora-release-notes 29-0

# Remove in F34; retired in F32+
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1578359
%obsolete python2-rabbitvcs 0.17.1-13

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1750660
%obsolete python2-libxslt 1.1.33-3

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1676261
%obsolete zanata-platform 4.6.0-3
%obsolete zanata-client 4.6.0-3
%obsolete zanata-platform-javadoc 4.6.0-3

%description
This package exists only to obsolete other packages which need to be removed
from the distribution for some reason.

Currently obsoleted packages:

%list_obsoletes


%prep
%autosetup -c -T
cp %SOURCE0 .


%files
%doc README


%changelog
* Sun May 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 31-43
- Bump packages that were updated in F30, but still gone in F31 (#1833816)
- Add more Python 2 packages (#1833816)

* Fri May 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 31-42
- Bump versions on python2-matplotlib-* Obsoletes

* Tue Dec 03 2019 Miro Hrončok <mhroncok@redhat.com> - 31-41
- Obsolete python2-os-client-config (#1747436)
- Obsolete python2-simplemediawiki (#1767495)
- Obsolete python2-pep8 (#1779378)

* Wed Nov 27 2019 Kalev Lember <klember@redhat.com> - 31-40
- Remove gedit-plugin-synctex obsolete as it was re-added in gedit-plugins 3.34.1

* Thu Nov 21 2019 Miro Hrončok <mhroncok@redhat.com> - 31-39
- Obsolete python2-migrate (#1775389)

* Thu Nov  7 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 31-38
- Also obsolete other binary packages of zanata-platform

* Wed Oct 30 2019 Adam Williamson <awilliam@redhat.com> - 31-37
- Bump versions on Python 2 FreeIPA package obsoletes

* Sat Oct 26 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 31-36
- Obsolete zanata-platform

* Wed Oct 23 2019 Miro Hrončok <mhroncok@redhat.com> - 31-35
- Obsolete system-config-users-docs (#1751252)

* Fri Sep 20 2019 Pete Walter <pwalter@fedoraproject.org> - 31-34
- Bump python2-policycoreutils obsoletes version

* Wed Sep 18 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 31-33
- Obsolete fedora-release-notes, mono-debugger, python2-pillow-{tk,qt}

* Thu Sep 12 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 31-32
- Obsolete a bunch of python2 packages based on testing the upgrade
  path from F30 to F31.

* Thu Sep 12 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 31-31
- Obsolete a bunch of packages based on fedora-devel feedback
  (#1751418, #1751419, #1751345)

* Wed Sep 11 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 31-30
- Obsolete a bunch of packages (#1684162, #1750135, #1751211,
				##1750138, #1578359)

* Wed Sep 11 2019 Miro Hrončok <mhroncok@redhat.com> - 31-29
- Fix a typo in gcompris (#1747430)

* Tue Sep  3 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 31-28
- Obsolete fedmsg-notify (#1644813), gcompris (#1747430)

* Tue Sep  3 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 31-27
- Obsolete python2-pandas-datareader

* Tue Sep  3 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 31-26
- Obsolete gegl (#1747428)

* Fri Aug 30 2019 Miro Hrončok <mhroncok@redhat.com> - 31-25
- Obsolete python2-cliff, python2-copr, python2-docker, python2-fedmsg,
  python2-future, python2-grokmirror, python2-keystoneauth1, python2-markdown,
  python2-openstacksdk, python2-pwquality, python2-warlock, system-config-users
  (#1747436)

* Mon Aug 26 2019 Neal Gompa <ngompa13@gmail.com> - 31-24
- Obsolete oggconvert

* Sun Aug 25 2019 Kalev Lember <klember@redhat.com> - 31-23
- Obsolete gedit-plugin-synctex

* Sun Aug 25 2019 Kalev Lember <klember@redhat.com> - 31-22
- Obsolete python2-unbound

* Mon Aug 19 2019 Kalev Lember <klember@redhat.com> - 31-21
- Obsolete python2-libselinux and python2-libsemanage

* Tue Aug 13 2019 Miro Hrončok <mhroncok@redhat.com> - 31-20
- Obsolete a batch of problematic python2 packages removed in Fedora 31

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 31-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Miro Hrončok <mhroncok@redhat.com> - 31-18
- Obsolete python2-langtable (#1706075)

* Tue May 21 2019 Miro Hrončok <mhroncok@redhat.com> -31-17
- Obsolete yumex (#1707567)
- Obsolete pix (#1707570)
- Obsolete system-config-services (#1707577)

* Thu May 09 2019 Miro Hrončok <mhroncok@redhat.com> - 31-16
- Bump python2-hawkey, python2-libdnf and python2-solv versions (#1632564)

* Thu Apr 25 2019 Kalev Lember <klember@redhat.com> - 31-15
- Obsolete california (#1702954)

* Mon Apr 22 2019 Miro Hrončok <mhroncok@redhat.com> - 31-14
- No longer obsolete python2-blockdiag (#1699834)

* Tue Apr 16 2019 Orion Poplawski <orion@nwra.com> - 31-13
- Obsolete python2-envisage (#1700310)

* Tue Apr 16 2019 Miro Hrončok <mhroncok@redhat.com> - 31-12
- Obsolete mongodb, mongodb-server, mongodb-test < 4.0.3-4 (#1700073)
- Obsolete python2-certbot < 0.31.0-3 and python2-josepy < 1.1.0-7 (#1700045)

* Mon Apr 15 2019 Kevin Fenzi <kevin@scrye.com> - 31-11
- Obsolete mongodb < 4.0.3-3 (#1700073)

* Mon Apr 15 2019 Miro Hrončok <mhroncok@redhat.com> - 31-10
- Obsolete python2-cinderclient < 3.5.0-2

* Sun Apr 14 2019 Miro Hrončok <mhroncok@redhat.com> - 31-9
- Obsolete python2-testify < 0.11.0-13

* Thu Apr 11 2019 Fabio Valentini <decathorpe@gmail.com> - 31-8
- Add obsoletes for appcenter* packages.

* Wed Apr 10 2019 Kalev Lember <klember@redhat.com> - 31-7
- Remove gnome-books obsoletes now that the package is back in Fedora (#1698489)

* Mon Apr 08 2019 Miro Hrončok <mhroncok@redhat.com> - 31-6
- Obsolete another batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Apr 04 2019 Miro Hrončok <mhroncok@redhat.com> - 31-5
- Obsolete another batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal
- Obsolete python2-pylint (#1686848)
- Obsolete python2 subpackages of ceph (#1687998)

* Thu Apr 04 2019 Kalev Lember <klember@redhat.com> - 31-4
- Obsolete PyXB (#1696209)

* Fri Mar 08 2019 Miro Hrončok <mhroncok@redhat.com> - 31-3
- Obsolete Python 2 Sphinx packages
  https://fedoraproject.org/wiki/Changes/Sphinx2

* Mon Mar 04 2019 Miro Hrončok <mhroncok@redhat.com> - 31-2
- Obsolete another batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Feb 22 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 31-1
- Cleaned up for F31.
- Obsolete empathy (bz 1680068).

* Tue Feb 19 2019 Pete Walter <pwalter@fedoraproject.org> - 30-28
- Bump librepo and libcomps python2 subpackage obsoletes versions

* Tue Feb 19 2019 Pete Walter <pwalter@fedoraproject.org> - 30-27
- Bump dnf python2 subpackage obsoletes versions

* Tue Feb 19 2019 Bastien Nocera <bnocera@redhat.com> - 30-26
- Obsolete gnome-books after split off from gnome-documents

* Wed Feb 13 2019 Björn Esser <besser82@fedoraproject.org> - 30-25
- Obsolete trafficserver < 5.3.0-14 and its sub-packages

* Tue Feb 12 2019 Kalev Lember <klember@redhat.com> - 30-24
- Obsolete python-xpyb-devel as well, in addition to python2-xpyb

* Tue Feb 12 2019 Kalev Lember <klember@redhat.com> - 30-23
- Obsolete vala-compat

* Mon Feb 11 2019 Kalev Lember <klember@redhat.com> - 30-22
- Obsolete python2-isort

* Fri Feb 08 2019 Kalev Lember <klember@redhat.com> - 30-21
- Obsolete wxGTK and its subpackages

* Thu Feb 07 2019 Miro Hrončok <mhroncok@redhat.com> - 30-20
- Obsolete another batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Jan 31 2019 Pete Walter <pwalter@fedoraproject.org> - 30-19
- Obsolete python2-samba

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 30-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Pete Walter <pwalter@fedoraproject.org> - 30-17
- Obsolete python2-librepo

* Tue Jan 29 2019 Pete Walter <pwalter@fedoraproject.org> - 30-16
- Obsolete python2-bodhi and python2-bodhi-client
- Bump dnf-plugins-core python2 package obsoletes versions

* Thu Jan 10 2019 Kalev Lember <klember@redhat.com> - 30-15
- Obsolete gedit-plugin-dashboard

* Sat Jan 05 2019 Pete Walter <pwalter@fedoraproject.org> - 30-14
- Fix python2-blockdev and python2-dnf-plugins obsolete versions

* Thu Dec 13 2018 Miro Hrončok <mhroncok@redhat.com> - 30-13
- Obsolete sixth batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Nov 23 2018 Miro Hrončok <mhroncok@redhat.com> - 30-12
- Obsolete fifth batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Nov 01 2018 Miro Hrončok <mhroncok@redhat.com> - 30-11
- Obsolete fourth batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Oct 05 2018 Miro Hrončok <mhroncok@redhat.com> - 30-10
- Obsolete fourth batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Sep 30 2018 Miro Hrončok <mhroncok@redhat.com> - 30-9
- Obsolete third batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Sep 18 2018 Miro Hrončok <mhroncok@redhat.com> - 30-8
- Obsolete second batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Sep 18 2018 Miro Hrončok <mhroncok@redhat.com> - 30-7
- Obsolete python2-mapnik (#1630222)
- Obsolete first batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Sep 11 2018 Scott Talbert <swt@techie.net> - 30-6
- Obsolete python2-libconcord, python2-pyqtgraph, python2-pyopengl-tk

* Mon Sep 03 2018 Miro Hrončok <mhroncok@redhat.com> - 30-5
- Obsolete python2-behave (#1624838)

* Wed Aug 22 2018 Miro Hrončok <mhroncok@redhat.com>
- Obsolete more python3 packages (#1610422)

* Mon Aug 20 2018 Miro Hrončok <mhroncok@redhat.com> - 30-3
- Bump up version of abrt packages

* Fri Aug 17 2018 Miro Hrončok <mhroncok@redhat.com> - 30-2
- Obsolete python3-svgwrite (#1610422) (#1605936)

* Thu Aug 16 2018 Miro Hrončok <mhroncok@redhat.com> - 30-1
- Fedora 30 bump (removed all no longer needed obsoletes)

* Thu Aug 16 2018 Miro Hrončok <mhroncok@redhat.com> - 29-17
- Obsolete python3-trollius-redis (#1610422) (#1606877)

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 29-16
- Obsolete vte3 (#1315425)

* Wed Aug 08 2018 Miro Hrončok <mhroncok@redhat.com> - 29-15
- Obsolete python3-ovirt-register (#1610422) (#1605819)

* Wed Aug 01 2018 Miro Hrončok <mhroncok@redhat.com> - 29-14
- Obsolete removed python3 packages (#1610422)

* Tue Jul 31 2018 Stephen Gallagher <sgallagh@redhat.com> - 29-13
- Obsolete rolekit

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 29-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Pete Walter <pwalter@fedoraproject.org> - 29-11
- Obsolete fedora-productimg-workstation
- Bump NetworkManager-glib and libnm-gtk obsoletes versions

* Wed Jun 06 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 29-10
- Add ppc64-utils (https://bugzilla.redhat.com/show_bug.cgi?id=1588130).

* Fri May 18 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 29-9
- Add abrt-related python2 packages.
- Clean up and add more documentation, since many provenpackagers are modifying
  this package without including the needed information.
- Remove the last F29 entries.
- Fix bogus date in %%changelog.

* Thu May 17 2018 Lubomir Rintel <lkundrak@v3.sk> - 29-8
- Bump version of libnm-glib packages to f28 updates

* Mon May 07 2018 Pete Walter <pwalter@fedoraproject.org> - 29-7
- Obsolete python2-caribou and python3-caribou as well (#1568670)

* Fri May  4 2018 Peter Robinson <pbrobinson@fedoraproject.org> 29-6
- Obsolete libmx and presence
- Obsolete clucene09-core xorg-x11-drv-freedreno

* Fri May 04 2018 Pete Walter <pwalter@fedoraproject.org> - 29-5
- Obsolete old caribou versions (#1568670)

* Tue Apr 24 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 29-4
- Remove a number of "Remove in F28" and "Remove in F29" entries.

* Mon Apr 23 2018 Lubomir Rintel <lkundrak@v3.sk> - 29-3
- Obsolete libnm-glib based packages

* Thu Apr 12 2018 Kalev Lember <klember@redhat.com> - 29-2
- Fix bind99 obsoletes versions, obsolete mozjs17-devel

* Thu Apr 12 2018 Peter Robinson <pbrobinson@fedoraproject.org> 29-1
- bind99, mozjs17, python2-zeroconf, python2-chromecast

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 28-2
- Add xulrunner obsoletes

* Mon Nov 13 2017 Pete Walter <pwalter@fedoraproject.org> - 28-1
- Obsolete compat-ImageMagick693, compat-libvpx1

* Wed Nov  8 2017 Peter Robinson <pbrobinson@fedoraproject.org> 27-10
- Obsolete  compat-gnutls28, libsilc, pam_pkcs11, python-dapp

* Fri Oct 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 27-9
- Obsoletes: kdegraphics-strigi-analyzer kfilemetadata
- bump libkexiv2 version

* Sat Oct 07 2017 Rex Dieter <rdieter@fedoraproject.org> - 27-8
- Obsolets: kf5-libkface (#1423813)

* Sat Oct 07 2017 Rex Dieter <rdieter@fedoraproject.org> - 27-7
- Obsoletes: strigi, libkexiv2 (#1498850)

* Tue Aug 29 2017 Kalev Lember <klember@redhat.com> - 27-6
- Add seed obsoletes

* Tue Aug 29 2017 Kalev Lember <klember@redhat.com> - 27-5
- Add hawkey and libhif obsoletes

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Adam Williamson <awilliam@redhat.com> - 27-3
- Add webkitgtk and webkitgtk3 (and -devel) - RHBZ #1443614

* Wed Jun 21 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 27-2
- Add various devassistant-related packages from https://bugzilla.redhat.com/show_bug.cgi?id=1463408

* Tue May 16 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 27-1
- Add perl ZMQ packages from https://bugzilla.redhat.com/show_bug.cgi?id=1451372

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 14 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 26-1
- Initial release; nothing to obsolete yet.
