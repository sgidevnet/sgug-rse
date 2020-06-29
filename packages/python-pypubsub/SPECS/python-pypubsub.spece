%global pypi_name pypubsub
%global src_name Pypubsub

Name:           python-%{pypi_name}
Version:        4.0.3
Release:        8%{?dist}
Summary:        Python Publish-Subscribe Package

License:        BSD
URL:            https://github.com/schollii/pypubsub
Source0:        https://github.com/schollii/%{pypi_name}/archive/v%{version}.tar.gz#/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%description
PyPubSub provides a publish - subscribe API that facilitates the development of
event-based / message-based applications. PyPubSub supports sending and
receiving messages between objects of an application. It is centered on the
notion of a topic; senders publish messages of a given topic, and listeners
subscribe to messages of a given topic. The package also supports a variety of
advanced features that facilitate debugging and maintaining pypubsub topics and
messages in larger applications.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
PyPubSub provides a publish - subscribe API that facilitates the development of
event-based / message-based applications. PyPubSub supports sending and
receiving messages between objects of an application. It is centered on the
notion of a topic; senders publish messages of a given topic, and listeners
subscribe to messages of a given topic. The package also supports a variety of
advanced features that facilitate debugging and maintaining pypubsub topics and
messages in larger applications.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
pushd tests/suite
PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHONDONTWRITEBYTECODE=1 py.test-%{python3_version}
popd


%files -n python3-%{pypi_name}
%doc README.rst src/pubsub/RELEASE_NOTES.txt
%license src/pubsub/LICENSE_BSD_Simple.txt
%{python3_sitelib}/%{src_name}*
%{python3_sitelib}/pubsub/

%changelog
* Sat Jun 27 2020 Scott Talbert <swt@techie.net> - 4.0.3-8
- Add missing BR for setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Scott Talbert <swt@techie.net> - 4.0.3-1
- New upstream release 4.0.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 6 2018 Scott Talbert <swt@techie.net> - 4.0.0-1
- Initial package.
