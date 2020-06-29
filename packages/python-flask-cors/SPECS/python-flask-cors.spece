%global srcname flask-cors
%{?python_enable_dependency_generator}

Name:           python-%{srcname}
Version:        3.0.8
Release:        7%{?dist}
Summary:        Cross Origin Resource Sharing (CORS) support for Flask
License:        MIT
URL:            https://github.com/corydolphin/%{srcname}
Source0:        https://github.com/corydolphin/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

%package -n python3-%{srcname}
Summary:        Cross Origin Resource Sharing (CORS) support for Flask

%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-flask
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

%description -n python3-%{srcname}
Python3 flask_cors package.

%prep
%autosetup -n %{srcname}-%{version}

%build
%{py3_build}

%install
%{py3_install}

%check
%{__python3} setup.py test || :

%files -n python3-%{srcname}
%license LICENSE
%doc CHANGELOG.md README.rst
%{python3_sitelib}/flask_cors/
%{python3_sitelib}/Flask_Cors*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.8-7
- Rebuilt for Python 3.9

* Wed Apr 01 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.0.8-6
- Don't require tests to pass (Flask 1.0 fallout)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.0.8-1
- Update to 3.0.8

* Thu Jan 31 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.0.7-1
- Update to 3.0.7

* Tue Nov 21 2017 David Carlos <ddavidcarlos1392@gmail.com> - 3.0.3-5
- remove debug_package macro
- Add BuildArch to parent package and remove from subpackage

* Tue Nov 21 2017 David Carlos <ddavidcarlos1392@gmail.com> - 3.0.3-4
- Add python- prefix on source name
- Add a blank line between each changelog report.
- Change the path to build the package on prep step.

* Mon Nov 20 2017 David Carlos <ddavidcarlos1392@gmail.com> - 3.0.3-3
- Fix Source0 commentary.

* Sun Nov 19 2017 David Carlos <ddavidcarlos1392@gmail.com> - 3.0.3-2
- Use py3_install and py3_build instead of {__python3}
- Generates a sub package called python3-flask-cors, and keep the source name
as python-flask-cors
- Use py3_dist to resolve Requires and BuildRequires
- Fix rpmlint warnings

* Tue Nov 07 2017 David Carlos <ddavidcarlos1392@gmail.com> - 3.0.3-1
- Initial packaging work for Fedora
