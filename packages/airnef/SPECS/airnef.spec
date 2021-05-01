%if 0%{?rhel} && 0%{?rhel} <= 7
%global python    python2
%global appdir    %python2_sitelib/%name
%global appresdir %python2_sitelib/%name/appresource
%else
%global python    python3
%global appdir    %python3_sitelib/%name
%global appresdir %python3_sitelib/%name/appresource
%endif


Name:           airnef
Version:        1.1
Release:        7%{?dist}
Summary:        Wireless download from your Nikon/Canon Camera

License:        GPLv3
URL:            http://www.testcams.com/airnef/
BuildArch:      noarch
Source0:        http://www.testcams.com/airnef/Version_%{version}/airnef_v%{version}_Source.zip

Patch0:         airnef-1.1-rpm-paths.patch

BuildRequires:  %python-devel

Requires:       %python-six
Requires:       %python-tkinter

%description
Open-source utility for downloading images and videos from WiFi-equipped
cameras.  Airnef supports all Nikon cameras that have built-in WiFi interfaces,
along with those using external Nikon WU-1a and WU-1b WiFi adapters, Canon and
Sony cameras.


%prep
%autosetup -p1 -n airnef

# six is available in fedora
rm six.py

# OSX only file is not needed
rm airnefcmd_OSX_Frozen_Wrapper.py

# TODO: ??
rm appresource/airnef.icns

for i in `grep -l -r '#!/usr/bin/env python'`; do
    sed -i '1 s|#!/usr/bin/env python.*||g' "$i"
done


%build


%install
mkdir -p %buildroot%appdir
for i in *.py *.pyw; do
    dest=${i/%pyw/py} # drop pyw suffixes
    install "$i" -p -m 644 %buildroot%appdir/"$dest"
done

mkdir -p %buildroot%appresdir
for i in appresource/*; do
    install "$i" -p -m 644 %buildroot%appresdir
done

cat > wrapper <<'EOF'
#! /bin/sh
exec %python %appdir/"$(basename "$0").py" "$@"
EOF

mkdir -p %buildroot%_bindir
install -m 755 wrapper %buildroot%_bindir/airnef
install -m 755 wrapper %buildroot%_bindir/airnefcmd


%files
%doc
%_bindir/*
%dir %appdir
%appdir/*.py
%if %python == python3
%appdir/__pycache__
%else
%appdir/*.pyo
%appdir/*.pyc
%endif
%dir %appresdir
%appresdir/*.ico
%appresdir/*.gif
%appresdir/*.xbm



%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Pavel Raiskup <praiskup@redhat.com> - 1.1-6
- require python3-tkinter (rhbz#1702714)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuilt for Python 3.7

* Wed May 30 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1-2
- silent rpmdiff complaints about python shebangs (review rhbz#1583475)

* Tue May 29 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1-1
- initial RPM packaging
