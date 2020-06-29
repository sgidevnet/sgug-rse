%global pypi_name arpeggio
Name:           python-%{pypi_name}
Version:        1.9.2
Release:        1%{?dist}
Summary:        Packrat parser interpreter

License:        MIT
URL:            https://github.com/igordejanovic/Arpeggio
Source0:        %url/archive/v%{version}/Arpeggio-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest-runner)

%description
Arpeggio is a recursive descent parser with memoization based on PEG grammars
(aka Packrat parser).

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Arpeggio is a recursive descent parser with memoization based on PEG grammars
(aka Packrat parser).


%prep
%autosetup -p1 -n Arpeggio-%{version}


%build
%py3_build


%install
%py3_install

%check
%pytest -v


%files -n python3-%{pypi_name}
%doc README.rst AUTHORS.md CHANGELOG.md THANKS.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/examples/
%{python3_sitelib}/Arpeggio-%{version}-py%{python3_version}.egg-info/


%changelog
* Mon Jun 01 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.9.2-1
- Update to 1.9.2 (#1756618)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-1
- Initial package
