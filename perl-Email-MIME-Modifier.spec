#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	MIME-Modifier
Summary:	Email::MIME::Modifier - modify Email::MIME objects easily
Summary(pl):	Email::MIME::Modifier - ³atwe modyfikowanie obiektów Email::MIME
Name:		perl-Email-MIME-Modifier
Version:	1.42
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3acf1c19da93334be37f3f9a288acd91
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-MIME >= 1.7
BuildRequires:	perl-Email-MIME-ContentType >= 1
BuildRequires:	perl-Email-MIME-Encodings >= 1.2
BuildRequires:	perl-Email-MessageID >= 1.2
BuildRequires:	perl-Email-Simple >= 1.9
%endif
# not autodetected
Requires:	perl-Email-MIME >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a number of useful methods for manipulating MIME messages.

%description -l pl
Pakiet dostarcza wiele u¿ytecznych metod do obróbki wiadomo¶ci MIME.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Email/MIME/*.pm
%{_mandir}/man3/*
