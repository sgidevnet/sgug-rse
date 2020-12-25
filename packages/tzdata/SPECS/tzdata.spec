Summary: Timezone data
Name: tzdata
Version: 2020a
%define tzdata_version 2020a
%define tzcode_version 2020a
Release: 1%{?dist}
License: Public Domain
URL: https://www.iana.org/time-zones
#Source0: ftp://ftp.iana.org/tz/releases/tzdata%{tzdata_version}.tar.gz
#Source1: ftp://ftp.iana.org/tz/releases/tzcode%{tzcode_version}.tar.gz

# Hack, take an archive from fc31 and untar it
Source0: tzdata-%{tzdata_version}-relativearchive.tar.gz

BuildRequires: rsync
BuildArchitectures: noarch

%description
This package contains data files with rules for various timezones around
the world.

%prep
%setup -n tzdata-%{tzdata_version} -c -T
mkdir archive
cd archive
tar xf %{SOURCE0}
cd ..
cp archive/doc/tzdata/* .
cp archive/licenses/tzdata/* .

%build
# Nothing to do

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}
rsync -avx archive/* $RPM_BUILD_ROOT%{_datadir}/

%files
%{_datadir}/zoneinfo
%license LICENSE
%doc README
%doc theory.html
%doc tz-link.html
%doc tz-art.html

%changelog
* Sat Aug 15 2020 Daniel Hams <daniel.hams@gmail.com> - 2020a-1
- Ugly work around for lack of glibc "tic" - just use a tarball.
