%global srcname rq

Name:           python-%{srcname}
Version:        1.2.2
Release:        2%{?dist}
Summary:        Simple, lightweight, library for creating background jobs, and processing them

License:        BSD
URL:            https://github.com/rq/rq
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
RQ (Redis Queue) is a simple Python library for queueing jobs
and processing them in the background with workers.
It is backed by Redis and it is designed to have a low barrier to entry.
It should be integrated in your web stack easily.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{_bindir}/rq
%{_bindir}/rqinfo
%{_bindir}/rqworker
%{python3_sitelib}/rq-*.egg-info/
%{python3_sitelib}/rq/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Initial package
