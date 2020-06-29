%global pypi_name tomlkit

%{?python_enable_dependency_generator}

%global common_description %{expand:
TOML Kit is a 0.5.0-compliant TOML library.

It includes a parser that preserves all comments, indentations,
whitespace and internal element ordering, and makes them accessible and
editable via an intuitive API.

You can also create new TOML documents from scratch using the provided
helpers.

Part of the implementation as been adapted, improved and fixed from
Molten.}

Name:           python-%{pypi_name}
Summary:        Style preserving TOML library
Version:        0.5.11
Release:        2%{?dist}
License:        MIT

URL:            https://github.com/sdispater/tomlkit
Source0:        %{pypi_source}

# fixup setup.py (remove tests package and tests package data)
Patch0:         00-setup-py-fixup.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m pytest tests/


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md

%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.11-2
- Rebuilt for Python 3.9

* Sat Feb 29 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.11-1
- rebuilt

* Fri Feb 28 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.10-1
- Update to version 0.5.10.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 19 2019 Fabio Valentini <decathorpe@gmail.com> - 0.5.8-1
- Update to version 0.5.8.

* Fri Oct 04 2019 Fabio Valentini <decathorpe@gmail.com> - 0.5.7-1
- Update to version 0.5.7.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Fabio Valentini <decathorpe@gmail.com> - 0.5.5-1
- Update to version 0.5.5.

* Sun Jun 30 2019 Fabio Valentini <decathorpe@gmail.com> - 0.5.4-1
- Update to version 0.5.4.

* Sat May 04 2019 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-4
- Use setup from setuptools, not distutils.core.

* Mon Feb 11 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.5.3-3
- Added check section.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-1
- Initial package.

