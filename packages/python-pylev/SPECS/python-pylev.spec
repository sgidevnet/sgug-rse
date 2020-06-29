%global pypi_name pylev

%{?python_enable_dependency_generator}

%global common_description %{expand:
A pure Python Levenshtein implementation that’s not freaking GPL’d.

Based off the Wikipedia code samples at
https://en.wikipedia.org/wiki/Levenshtein_distance.}

Name:           python-%{pypi_name}
Summary:        Liberally licensed, pure Python Levenshtein implementation
Version:        1.3.0
Release:        7%{?dist}
License:        BSD

URL:            http://github.com/toastdriven/pylev
Source0:        %{pypi_source}

# Include LICENSE file from upstream repository
Source1:        https://raw.githubusercontent.com/toastdriven/pylev/master/LICENSE

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

cp %{SOURCE1} .


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE

%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-1
- Initial package.

