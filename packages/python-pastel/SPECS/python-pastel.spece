%global pypi_name pastel

%{?python_enable_dependency_generator}

%global common_description %{expand:
Pastel is a simple library to help you colorize strings in your
terminal.

It comes bundled with predefined styles:

- info: green
- comment: yellow
- question: black on cyan
- error: white on red

Features:

- Use predefined styles or add you own.
- Disable colors all together by calling with_colors(False).
- Automatically disables colors if the output is not a TTY.
- Used in cleo.}

Name:           python-%{pypi_name}
Summary:        Bring colors to your terminal
Version:        0.2.0
Release:        2%{?dist}
License:        MIT

URL:            https://github.com/sdispater/pastel
Source0:        %{pypi_source}

# do not install the "tests" package
Patch0:         00-dont-install-tests.patch

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

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=. pytest tests


%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE

%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-1
- Update to version 0.2.0.
- Enable running test suite.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-2
- Rebuilt for Python 3.8

* Sat Aug 10 2019 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-1
- Initial package.

