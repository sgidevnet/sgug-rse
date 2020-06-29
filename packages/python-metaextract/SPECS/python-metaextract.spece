%global srcname metaextract

%global descr Metaextract is a tool to collect metadata about a Python \
module. For example you may have a sdist tarball from the Python Package Index \
and you want to know it's dependencies. metaextract can collect theses \
dependencies. The tool was first developed in py2pack but is now it's own \
module to be useful for others, too.

Name:           python-%{srcname}
Version:        1.0.7
Release:        3%{?dist}
Summary:        Metaextract is a tool to collect metadata for Python modules

License:        ASL 2.0
URL:            https://github.com/toabctl/metaextract
Source0:        %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
%descr

%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires: %{py3_dist mock}
BuildRequires: %{py3_dist pytest-runner}
BuildRequires: %{py3_dist pbr} >= 1.0

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%descr

%package        doc
Summary:        Documentation for %name
BuildRequires:  %{py3_dist sphinx}

%description    doc
Documentation for %name


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build
python3 setup.py build_sphinx

rm doc/build/html/objects.inv

%install
%py3_install

%check
export PYTHONPATH=$(pwd):$PYTHONPATH
python3 -m pytest metaextract

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/metaextract

%files doc
%license LICENSE
%doc doc/build/html/*

%changelog
* Sun May 31 2020 Dan Čermák <dan@Eclipse> - 1.0.7-3
- Drop unnecessary BuildRequire python3-flak8 (rhbz#1841733)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-2
- Rebuilt for Python 3.9

* Thu Apr  9 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.7-1
- New upstream release 1.0.7 (rhbz#1818616)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.6-2
- Add missing BuildRequire pbr

* Sun Sep  8 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.6-1
- Bump version to 1.0.6

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar  6 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.5-1
- Initial package version
