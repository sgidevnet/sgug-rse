# Created by pyp2rpm-3.3.2
%global pypi_name towncrier

%global common_description %{expand:
Towncrier is a utility to produce useful, summarised news files for your 
project. Rather than reading the Git history as some newer tools to produce it,
or having one single file which developers all write to, towncrier reads "news 
fragments" which contain information useful to end users.}

Name:           python-%{pypi_name}
Version:        19.2.0
Release:        8%{?dist}
Summary:        Building newsfiles for your project

License:        MIT
URL:            https://github.com/hawkowl/towncrier
Source0:        %pypi_source
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(incremental)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(toml)

%bcond_without tests
%if %{with tests}
BuildRequires:  python3dist(twisted)
BuildRequires:  git-core
%endif

%{?python_enable_dependency_generator}

%description
%{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       %{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}
%{common_description}


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install

%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:$PYTHONPATH  %{_bindir}/trial towncrier
%endif


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/towncrier
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 19.2.0-8
- Rebuilt for Python 3.9

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 19.2.0-7
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 19.2.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 19.2.0-4
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 19.2.0-3
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Robert-André Mauchin <zebob.m@gmail.com> - 19.2.0-1
- Release 19.2.0
- Run tests

* Tue Feb 26 2019 Miro Hrončok <mhroncok@redhat.com> - 17.8.0-6
- Provide towncrier

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 17.8.0-4
- Remove Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 17.8.0-2
- Rebuilt for Python 3.7

* Mon May 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 17.8.0-1
- Initial package.
