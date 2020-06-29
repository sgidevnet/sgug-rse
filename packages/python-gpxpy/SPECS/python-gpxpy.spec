%global srcname gpxpy

Name:           python-%{srcname}
Version:        1.4.2
Release:        1%{?dist}
Summary:        GPX file parser and GPS track manipulation library

License:        ASL 2.0
URL:            https://github.com/tkrajina/gpxpy
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%{summary}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} test.py


%files -n python3-%{srcname}
%doc README.md
%license LICENSE.txt
%{_bindir}/gpxinfo
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info


%changelog
* Mon Jun 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-1
- Update to latest version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-2
- Rebuilt for Python 3.9

* Sat May 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-1
- Update to latest version

* Tue Jan 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version
- Backport fix for Python 3.9

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.5-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 03 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.5-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.4-1
- Update to latest version

* Sun Aug 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.3-1
- Update to latest version

* Thu Jul 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Initial package.
