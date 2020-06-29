%global srcname ogr

Name:           python-%{srcname}
Version:        0.12.1
Release:        1%{?dist}
Summary:        One API for multiple git forges

License:        MIT
URL:            https://github.com/packit-service/ogr
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm-git-archive)

%description
One Git library to Rule!

%package -n     python3-%{srcname}
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides
%if 0%{?fedora} < 33
%{?python_provide:%python_provide python3-%{srcname}}
%endif

%description -n python3-%{srcname}
One Git library to Rule!


%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info


%changelog
* Thu Jun 11 2020 Dominika Hodovska <dhodovsk@redhat.com> - 0.12.1-1
- new upstream release: 0.12.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Frantisek Lachman <flachman@redhat.com> - 0.12.0-1
- new upstream release: 0.12.0

* Mon Apr 27 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.11.3-1
- new upstream release: 0.11.3

%autochangelog
