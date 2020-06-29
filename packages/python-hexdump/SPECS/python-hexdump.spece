%global         hguser         techtonik
%global         srcname        hexdump
# 2016-08-18
%global         commit         66325cb5fed890df4a345e25ea8f107fd31b60d8
%global         commitdate     20160818
%global         shortcommit    %(c=%{commit}; echo ${c:0:12})


Name:           python-hexdump
Version:        3.4
Release:        0.12.%{commitdate}hg%{shortcommit}%{?dist}
Summary:        Dump binary data to hex format and restore from there

License:        Public Domain
#               https://pypi.python.org/pypi/hexdump
#               https://bitbucket.org/techtonik/hexdump
URL:            https://bitbucket.com/%{hguser}/%{srcname}
Source0:        https://bitbucket.org/%{hguser}/%{srcname}/get/%{shortcommit}.zip#/%{name}-%{version}-%{shortcommit}.zip
Source1:        hexdumpy.1

# Create the /usr/bin/hexdumpy
# https://bitbucket.org/techtonik/hexdump/pull-requests/5/modify-the-setuppy-in-order-to-generate/diff
Patch0:         %{name}-setup.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
Python library to dump binary data to hex format and restore from there



%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Dump binary data to hex format and restore from there
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Python library to dump binary data to hex format and restore from there



%prep
%setup -q -n %{hguser}-%{srcname}-%{shortcommit}
%patch0 -p 1 -b .setup
sed -i -e 's|#!/usr/bin/env python|#|' hexdump.py


%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/hexdumpy.1

%files -n python%{python3_pkgversion}-%{srcname}
%license UNLICENSE
%doc README.txt
%{python3_sitelib}/*
%{_bindir}/hexdumpy
%{_mandir}/man1/hexdumpy.1*



%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4-0.12.20160818hg66325cb5fed8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.11.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4-0.10.20160818hg66325cb5fed8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4-0.9.20160818hg66325cb5fed8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.8.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.7.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.4-0.6.20160818hg66325cb5fed8
- Subpackage python2-hexdump has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-0.5.20160818hg66325cb5fed8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4-0.4.20160818hg66325cb5fed8
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.4-0.3.20160818hg66325cb5fed8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 4 2018 Michal Ambroz <rebus _AT seznam.cz> - 3.4-0.2.20160818hg66325cb5fed8
- fix python package directory based on package review

* Wed Dec 13 2017 Michal Ambroz <rebus _AT seznam.cz> - 3.4-0.1.20160818hg66325cb5fed8
- fixes during the package review, fix versioning, add manpage

* Wed Oct 04 2017 Michal Ambroz <rebus _AT seznam.cz> - 3.3-1
- Initial package for Fedora
