%global pkg lookup
%global pkgname Lookup

Name:		emacs-%{pkg}
Version:	1.4.1
Release:	19%{?dist}
Summary:	Search Interface with Electronic Dictionaries for Emacs
Summary(ja):	Emacs 上で動作する辞書検索インターフェイス

License:	GPLv2+
URL:		http://openlab.ring.gr.jp/edict/lookup/
Source0:	http://openlab.ring.gr.jp/edict/lookup/dist/%{pkg}-%{version}.tar.gz
Patch0:		lookup-lisp-makefile-am.patch
Patch1:		lookup-lisp-ndic-el-typo.patch

BuildArch:	noarch
BuildRequires:	emacs, automake
Requires:	emacs(bin) >= %{_emacs_version}
Requires(post): info
Requires(preun): info
Provides:	emacs-%{pkg}-el = %{version}-%{release}
Obsoletes:	emacs-%{pkg}-el < %{version}-%{release}

%description
Lookup is an integrated search interface with electronic dictionaries
for the Emacs text editor. You can use various kinds of dictionaries,
such as CD-ROM books and online dictionaries, in an efficient and
effective manner.

%description -l ja
Lookup は Emacs エディタで利用できる辞書検索インターフェースです。市販
のCD-ROM 辞書やネットワークの辞書サーバを始め、様々な情報源から簡単な操
作と設定で辞書検索が行なえます。


%prep
%setup -q -n %{pkg}-%{version}
%patch0 -p0 -b .lisp-makefile-am
%patch1 -p1 -b .lisp-ndic-el-typo
for i in README NEWS texi/*.texi; do
    iconv -f ISO-2022-JP -t UTF-8 $i > $i.UTF-8
    mv $i.UTF-8 $i
done
autoreconf -f -i


%build
%configure
make %{?_smp_mflags}
cat > %{name}-init.el <<"EOF"
(autoload 'lookup "lookup" nil t)
(autoload 'lookup-region "lookup" nil t)
(autoload 'lookup-pattern "lookup" nil t)
EOF



%install
%__mkdir_p $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}
make install lispdir=$RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg} \
	infodir=$RPM_BUILD_ROOT%{_infodir}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir # don't package but instead update in pre and post

%__mkdir_p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
install -m 644 %{name}-init.el ${RPM_BUILD_ROOT}%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%doc AUTHORS COPYING NEWS README
%doc %{_infodir}/*.gz
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitestartdir}/*.el
%dir %{_emacs_sitelispdir}/%{pkg}


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Daiki Ueno <dueno@redhat.com> - 1.4.1-12
- drop -el subpackages (#1234544)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug  6 2012 Daiki Ueno <dueno@redhat.com> - 1.4.1-7
- fix typo which causes build failure with Emacs 24

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Daiki Ueno <dueno@redhat.com> - 1.4.1-3
- include COPYING in %%doc.
- add Japanese translations of summary and description sections.

* Fri Oct 29 2010 Daiki Ueno <dueno@redhat.com> - 1.4.1-2
- convert encoding of *.texi to UTF-8.

* Thu Oct 28 2010 Daiki Ueno <dueno@redhat.com> - 1.4.1-1
- repackage version 1.4.1 maintained by the edict project, instead of
  1.99 beta.

* Tue Apr  6 2010 Daiki Ueno <ueno@unixuser.org> - 1.99.95-1
- initial packaging for Fedora.
