%global commit0 b1b2b298b85a795239daad84c75be073ddc4f8bd
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global snapdate 20200625

%global srcname migen

Name:           python-%{srcname}
Version:        0.9.2
Release:        4.%{snapdate}git%{shortcommit0}%{?dist}
Summary:        A Python toolbox for building complex digital hardware

License:        BSD
URL:            https://m-labs.hk/%{srcname}
Source0:        https://github.com/m-labs/%{srcname}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist colorama}
BuildRequires:  python-sphinx-latex
BuildRequires:  latexmk

%description
Migen enables hardware designers to take advantage of the richness of
Python (object oriented programming, function parameters, generators,
operator overloading, libraries, etc.), to build well organized, reusable
and elegant digital hardware designs.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Migen enables hardware designers to take advantage of the richness of
Python (object oriented programming, function parameters, generators,
operator overloading, libraries, etc.), to build well organized, reusable
and elegant digital hardware designs.

%prep
%autosetup -n %{srcname}-%{commit0}
sed -r -i 's/(migen_version = ).*/\1"%{version}-%{release}"/' doc/conf.py

%build
%py3_build
PYTHONPATH=. sphinx-build-3 -M latexpdf doc _build/pdf
PYTHONPATH=. sphinx-build-3 -b man doc _build/man

%install
%py3_install
install -Dpm644 -t %{buildroot}%{_mandir}/man1 _build/man/%{srcname}.1

%check
%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license LICENSE
%doc README.md _build/pdf/latex/Migen.pdf
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/
%{_mandir}/man1/%{srcname}.1*

%changelog
* Thu Jun 25 2020 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-4.20200625gitb1b2b29
- added setuptools build dependency
- updated to latest snapshot

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-3.20191204git4c00f5b
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2.20191204git4c00f5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-1.20191204git4c00f5b
- Update to 0.9.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-4.20190606git562c046
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-3.20190606git562c046
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2.20190606git562c046
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.9.1-1.20190606git562c046
- Update to 0.9.1

* Mon May 20 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.8-0.4.20190520git9031bfe
- Update to newer snapshot.

* Mon Apr 15 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.8-0.3.20190415gitedcadbc
- Update to newer snapshot.

* Wed Feb 27 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.8-0.2.20190227git936732f
- Update to newer snapshot.

* Mon Feb 18 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.8-0.1.20190218gitafe4405
- Initial version.
